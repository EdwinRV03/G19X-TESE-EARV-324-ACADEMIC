
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Usuario
from app.security import (
    verificar_password,
    verificar_version_token,
    crear_token_acceso,
    verificar_token_acceso,
    generar_hash_password
)
from app.services_email import enviar_correo
from app.services_recuperacion import (
    generar_token_recuperacion,
    calcular_hash_token,
    token_esta_vigente
)
from app.models import TokenRecuperacion
from datetime import datetime, timedelta, timezone

router = APIRouter(prefix="/auth", tags=["Autenticación"])
bearer_scheme = HTTPBearer(auto_error=False)


class SolicitudLogin(BaseModel):
    email: EmailStr
    password: str

class SolicitudCrearUsuario(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class SolicitudEditarUsuario(BaseModel):
    nombre: str
    email: EmailStr

class SolicitudCambiarPassword(BaseModel):
    password_actual: str
    password_nueva: str

class SolicitudRecuperacion(BaseModel):
    email: EmailStr

class SolicitudRestablecerPassword(BaseModel):
    token: str
    password_nueva: str

def obtener_usuario_actual(
    credenciales: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    if credenciales is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Se requiere iniciar sesión",
            headers={"WWW-Authenticate": "Bearer"}
        )

    usuario_id = verificar_token_acceso(credenciales.credentials)

    if usuario_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"}
        )

    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if (
        not usuario
        or not usuario.activo
        or usuario.rol not in ("admin", "usuario")
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no autorizado o cuenta desactivada",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not verificar_version_token(
        credenciales.credentials,
        usuario.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="La sesión ha expirado o fue invalidada",
            headers={"WWW-Authenticate": "Bearer"}
        )

    return usuario


@router.post("/login")
def iniciar_sesion(
    datos: SolicitudLogin,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.email == str(datos.email).lower()
    ).first()

    if not usuario or not verificar_password(
        datos.password, usuario.password_hash
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if usuario.rol not in ("admin", "usuario"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario no tiene un rol autorizado"
        )

    if not usuario.activo:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="La cuenta está desactivada"
        )

    token = crear_token_acceso(usuario.id, usuario.password_hash)

    return {
        "access_token": token,
        "token_type": "bearer",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol
        }
    }


@router.get("/me")
def obtener_mi_perfil(
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "email": usuario.email,
        "rol": usuario.rol
    }

def requerir_administrador(
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    if usuario.rol != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos de administrador"
        )

    return usuario

@router.post("/usuarios", status_code=status.HTTP_201_CREATED)
def crear_usuario(
    datos: SolicitudCrearUsuario,
    administrador: Usuario = Depends(requerir_administrador),
    db: Session = Depends(get_db)
):
    nombre = datos.nombre.strip()
    email = str(datos.email).strip().lower()

    if not nombre or len(nombre) > 100:
        raise HTTPException(
            status_code=422,
            detail="El nombre debe contener entre 1 y 100 caracteres"
        )

    if len(datos.password) < 8:
        raise HTTPException(
            status_code=422,
            detail="La contraseña debe tener al menos 8 caracteres"
        )

    if len(datos.password) > 128:
        raise HTTPException(
            status_code=422,
            detail="La contraseña no puede superar los 128 caracteres"
        )

    usuario_existente = db.query(Usuario).filter(
        Usuario.email == email
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=409,
            detail="Ya existe un usuario registrado con ese correo"
        )

    nuevo_usuario = Usuario(
        nombre=nombre,
        email=email,
        password_hash=generar_hash_password(datos.password),
        rol="usuario"
    )

    try:
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception:
        db.rollback()
        raise

    return {
        "mensaje": "Usuario creado correctamente",
        "usuario": {
            "id": nuevo_usuario.id,
            "nombre": nuevo_usuario.nombre,
            "email": nuevo_usuario.email,
            "rol": nuevo_usuario.rol
        }
    }

@router.get("/usuarios")
def listar_usuarios(
    administrador: Usuario = Depends(requerir_administrador),
    db: Session = Depends(get_db)
):
    usuarios = db.query(Usuario).order_by(Usuario.id.asc()).all()

    return [
        {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol,
            "activo": usuario.activo
        }
        for usuario in usuarios
    ]

@router.put("/usuarios/{usuario_id}")
def editar_usuario(
    usuario_id: int,
    datos: SolicitudEditarUsuario,
    administrador: Usuario = Depends(requerir_administrador),
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    nombre = datos.nombre.strip()
    email = str(datos.email).strip().lower()

    if not nombre or len(nombre) > 100:
        raise HTTPException(
            status_code=422,
            detail="El nombre debe tener entre 1 y 100 caracteres"
        )

    if len(email) > 100:
        raise HTTPException(
            status_code=422,
            detail="El correo no puede superar los 100 caracteres"
        )

    correo_existente = db.query(Usuario).filter(
        Usuario.email == email,
        Usuario.id != usuario_id
    ).first()

    if correo_existente:
        raise HTTPException(
            status_code=409,
            detail="El correo ya pertenece a otro usuario"
        )

    usuario.nombre = nombre
    usuario.email = email

    try:
        db.commit()
        db.refresh(usuario)
    except Exception:
        db.rollback()
        raise

    return {
        "mensaje": "Usuario actualizado correctamente",
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol
        }
    }

@router.patch("/usuarios/{usuario_id}/estado")
def cambiar_estado_usuario(
    usuario_id: int,
    administrador: Usuario = Depends(requerir_administrador),
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    if usuario.id == administrador.id:
        raise HTTPException(
            status_code=403,
            detail="No puedes cambiar el estado de tu propia cuenta"
        )

    if usuario.rol == "admin":
        raise HTTPException(
            status_code=403,
            detail="No puedes cambiar el estado de otro administrador"
        )

    usuario.activo = not usuario.activo

    try:
        db.commit()
        db.refresh(usuario)
    except Exception:
        db.rollback()
        raise

    return {
        "mensaje": (
            "Usuario activado correctamente"
            if usuario.activo
            else "Usuario desactivado correctamente"
        ),
        "usuario": {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "rol": usuario.rol,
            "activo": usuario.activo
        }
    }

@router.post("/cambiar-password")
def cambiar_password(
    datos: SolicitudCambiarPassword,
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    if not verificar_password(
        datos.password_actual,
        usuario_actual.password_hash
    ):
        raise HTTPException(
            status_code=400,
            detail="La contraseña actual es incorrecta"
        )

    if len(datos.password_nueva) < 8:
        raise HTTPException(
            status_code=422,
            detail="La nueva contraseña debe tener al menos 8 caracteres"
        )

    if len(datos.password_nueva) > 128:
        raise HTTPException(
            status_code=422,
            detail="La nueva contraseña no puede superar los 128 caracteres"
        )

    if verificar_password(
        datos.password_nueva,
        usuario_actual.password_hash
    ):
        raise HTTPException(
            status_code=400,
            detail="La nueva contraseña debe ser diferente de la actual"
        )

    usuario_actual.password_hash = generar_hash_password(
        datos.password_nueva
    )

    try:
        db.commit()
    except Exception:
        db.rollback()
        raise

    return {
        "mensaje": "Contraseña actualizada correctamente"
    }

@router.post("/solicitar-recuperacion")
def solicitar_recuperacion(
    datos: SolicitudRecuperacion,
    db: Session = Depends(get_db)
):
    mensaje_generico = {
        "mensaje": "Si el correo está registrado y activo, recibirás instrucciones de recuperación."
    }

    email = str(datos.email).strip().lower()

    usuario = db.query(Usuario).filter(
        Usuario.email == email,
        Usuario.activo.is_(True)
    ).first()

    if usuario is None:
        return mensaje_generico

    ahora = datetime.now(timezone.utc).replace(tzinfo=None)

    ultimo_token = (
        db.query(TokenRecuperacion)
        .filter(TokenRecuperacion.usuario_id == usuario.id)
        .order_by(TokenRecuperacion.id.desc())
        .first()
    )

    if ultimo_token is not None:
        fecha_creacion_aproximada = (
            ultimo_token.fecha_expiracion - timedelta(minutes=15)
        )

        if ahora - fecha_creacion_aproximada < timedelta(seconds=60):
            return mensaje_generico

    token, token_hash, expiracion = generar_token_recuperacion()

    registro = TokenRecuperacion(
        usuario_id=usuario.id,
        token_hash=token_hash,
        fecha_expiracion=expiracion,
        utilizado=False
    )

    db.add(registro)
    db.commit()

    enlace = (
        "http://localhost:5173/"
        f"?recuperar_token={token}"
    )

    try:
        enviar_correo(
            destinatario=usuario.email,
            asunto="Recuperación de contraseña - Sistema de Notificaciones Legales",
            contenido=(
                "Recibimos una solicitud para restablecer tu contraseña.\n\n"
                f"Abre el siguiente enlace:\n{enlace}\n\n"
                "El enlace vence en 15 minutos y solo puede utilizarse una vez.\n\n"
                "Si no solicitaste este cambio, ignora este mensaje."
            )
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=503,
            detail="No fue posible procesar la solicitud en este momento."
        )

    return mensaje_generico

@router.post("/restablecer-password")
def restablecer_password(
    datos: SolicitudRestablecerPassword,
    db: Session = Depends(get_db)
):
    error_token = HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="El enlace es inválido, ya fue utilizado o ha expirado"
    )

    if not datos.token or len(datos.token) > 256:
        raise error_token

    if not 8 <= len(datos.password_nueva) <= 128:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="La contraseña debe tener entre 8 y 128 caracteres"
        )

    token_hash = calcular_hash_token(datos.token)

    try:
        registro = (
            db.query(TokenRecuperacion)
            .filter(TokenRecuperacion.token_hash == token_hash)
            .with_for_update()
            .first()
        )

        if (
            registro is None
            or registro.utilizado
            or not token_esta_vigente(registro.fecha_expiracion)
        ):
            raise error_token

        usuario = (
            db.query(Usuario)
            .filter(Usuario.id == registro.usuario_id)
            .first()
        )

        if usuario is None or not usuario.activo:
            raise error_token

        if verificar_password(
            datos.password_nueva,
            usuario.password_hash
        ):
            raise HTTPException(
                status_code=400,
                detail="La nueva contraseña debe ser diferente de la actual"
            )

        usuario.password_hash = generar_hash_password(
            datos.password_nueva
        )

        registro.utilizado = True

        db.commit()

    except Exception:
        db.rollback()
        raise

    return {
        "mensaje": "Contraseña restablecida correctamente"
    }
