import base64
import traceback
from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Dict, Any, Optional
from app.auth import router as auth_router
from app.auth import obtener_usuario_actual
from app.database import engine, Base, get_db, SessionLocal
from app.models import Plantilla, DocumentoGenerado, Usuario, VersionDocumento
from app.services_ai import generar_redaccion_legal
from app.plantillas import plantillas
from app.services_export import exportar_a_pdf, exportar_a_docx

Base.metadata.create_all(bind=engine)

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    try:
        plantillas(db)
    finally:
        db.close()

    yield

app = FastAPI(
    title="Sistema de Notificaciones Legales",
    lifespan=lifespan
)

app.include_router(auth_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SolicitudBorrador(BaseModel):
    plantilla_id: int
    datos_variables: Dict[str, Any]

class SolicitudGuardar(BaseModel):
    plantilla_id: int
    contenido: str
    datos_variables: Dict[str, Any]

class SolicitudEditarDocumento(BaseModel):
    contenido: str
    datos_variables: Optional[Dict[str, Any]] = None
    version_actual: int

@app.get("/plantillas/", dependencies=[Depends(obtener_usuario_actual)])
def listar_plantillas(db: Session = Depends(get_db)):
    try:
        return (
            db.query(Plantilla)
            .order_by(Plantilla.id.asc())
            .all()
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="No fue posible consultar las plantillas."
        )

@app.post("/documentos/redactar-borrador/", dependencies=[Depends(obtener_usuario_actual)])
def redactar_borrador(solicitud: SolicitudBorrador, db: Session = Depends(get_db)):
    plantilla = db.query(Plantilla).filter(Plantilla.id == solicitud.plantilla_id).first()
    if not plantilla:
        raise HTTPException(status_code=404, detail="Plantilla no encontrada")

    try:
        contenido = generar_redaccion_legal(plantilla.cuerpo_base, solicitud.datos_variables)
        return {"status": "borrador_generado", "contenido_generado": contenido}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar borrador con IA: {str(e)}")


@app.post("/documentos/guardar/")
def guardar_documento(
    solicitud: SolicitudGuardar,
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    plantilla = db.query(Plantilla).filter(
        Plantilla.id == solicitud.plantilla_id
    ).first()

    if not plantilla:
        raise HTTPException(
            status_code=404,
            detail="Plantilla no encontrada"
        )

    doc = DocumentoGenerado(
        plantilla_id=plantilla.id,
        datos_variables=solicitud.datos_variables,
        usuario_id=usuario_actual.id,
        contenido=solicitud.contenido,
        estado="confirmado"
    )

    db.add(doc)
    db.commit()
    db.refresh(doc)

    return {
        "status": "guardado",
        "documento_id": doc.id,
        "titulo_plantilla": plantilla.titulo
    }

@app.put("/documentos/{documento_id}/editar")
def editar_documento(
    documento_id: int,
    solicitud: SolicitudEditarDocumento,
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    if not solicitud.contenido.strip():
        raise HTTPException(
            status_code=422,
            detail="El contenido del documento no puede estar vacío."
        )

    try:
        documento = (
            db.query(DocumentoGenerado)
            .filter(DocumentoGenerado.id == documento_id)
            .with_for_update()
            .first()
        )

        if documento is None:
            raise HTTPException(
                status_code=404,
                detail="Documento no encontrado."
            )

        if (
            usuario_actual.rol != "admin"
            and documento.usuario_id != usuario_actual.id
        ):
            raise HTTPException(
                status_code=403,
                detail="No tienes permiso para editar este documento."
            )

        if documento.version != solicitud.version_actual:
            raise HTTPException(
                status_code=409,
                detail="El documento fue modificado. Actualiza el historial antes de editar."
            )

        version_anterior = VersionDocumento(
            documento_id=documento.id,
            version=documento.version,
            contenido=documento.contenido,
            datos_variables=documento.datos_variables
        )

        db.add(version_anterior)

        documento.contenido = solicitud.contenido

        if solicitud.datos_variables is not None:
            documento.datos_variables = solicitud.datos_variables

        documento.version += 1

        db.commit()
        db.refresh(documento)

        return {
            "mensaje": "Documento actualizado correctamente.",
            "documento_id": documento.id,
            "version": documento.version
        }

    except HTTPException:
        db.rollback()
        raise

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail="No fue posible actualizar el documento."
        )

@app.get("/documentos/{documento_id}/versiones")
def consultar_versiones_documento(
    documento_id: int,
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    documento = (
        db.query(DocumentoGenerado)
        .filter(DocumentoGenerado.id == documento_id)
        .first()
    )

    if documento is None:
        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado."
        )

    if (
        usuario_actual.rol != "admin"
        and documento.usuario_id != usuario_actual.id
    ):
        raise HTTPException(
            status_code=403,
            detail="No tienes permiso para consultar este documento."
        )

    versiones = (
        db.query(VersionDocumento)
        .filter(VersionDocumento.documento_id == documento_id)
        .order_by(VersionDocumento.version.asc())
        .all()
    )

    resultado = [
        {
            "version": v.version,
            "contenido": v.contenido,
            "datos_variables": v.datos_variables,
            "fecha_version": v.fecha_version
        }
        for v in versiones
    ]

    resultado.append({
        "version": documento.version,
        "contenido": documento.contenido,
        "datos_variables": documento.datos_variables,
        "fecha_version": documento.fecha_creacion,
        "actual": True
    })

    return {
        "documento_id": documento.id,
        "versiones": resultado
    }

@app.get("/documentos/")
def listar_documentos(
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    consulta = db.query(DocumentoGenerado)

    if usuario_actual.rol != "admin":
        consulta = consulta.filter(
            DocumentoGenerado.usuario_id == usuario_actual.id
        )

    docs = consulta.order_by(
        DocumentoGenerado.id.desc()
    ).all()

    resultado = []

    for d in docs:
        resultado.append({
            "documento_id": d.id,
            "plantilla_id": d.plantilla_id,
            "titulo_plantilla": d.plantilla.titulo if d.plantilla else "Carta Legal",
            "estado": d.estado,
            "version": d.version,
            "contenido": d.contenido,
            "datos_variables": d.datos_variables
        })

    return resultado


@app.post("/documentos/{documento_id}/exportar/pdf")
async def exportar_pdf_con_logo(
    documento_id: int,
    logo_pos: str = Form("ninguno"),
    file: Optional[UploadFile] = File(None),
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    doc = db.query(DocumentoGenerado).filter(DocumentoGenerado.id == documento_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    if usuario_actual.rol != "admin" and doc.usuario_id != usuario_actual.id:
        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado"
        )

    try:
        logo_bytes = await file.read() if file else None
        pdf_bytes = exportar_a_pdf(doc.contenido, logo_bytes=logo_bytes, logo_pos=logo_pos)

        return Response(
            content=pdf_bytes,
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=notificacion_{documento_id}.pdf"}
        )
    except Exception as e:
        print("=== ERROR AL GENERAR PDF ===")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno PDF: {str(e)}")


@app.post("/documentos/{documento_id}/exportar/docx")
async def exportar_docx_con_logo(
    documento_id: int,
    logo_pos: str = Form("ninguno"),
    file: Optional[UploadFile] = File(None),
    usuario_actual: Usuario = Depends(obtener_usuario_actual),
    db: Session = Depends(get_db)
):
    doc = db.query(DocumentoGenerado).filter(DocumentoGenerado.id == documento_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    if usuario_actual.rol != "admin" and doc.usuario_id != usuario_actual.id:
        raise HTTPException(
            status_code=404,
            detail="Documento no encontrado"
        )

    try:
        logo_bytes = await file.read() if file else None
        docx_bytes = exportar_a_docx(doc.contenido, logo_bytes=logo_bytes, logo_pos=logo_pos)

        return Response(
            content=docx_bytes,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename=notificacion_{documento_id}.docx"}
        )
    except Exception as e:
        print("=== ERROR AL GENERAR DOCX ===")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Error interno DOCX: {str(e)}")
