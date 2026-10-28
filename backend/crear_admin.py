
from getpass import getpass

from app.database import SessionLocal
from app.models import Usuario
from app.security import generar_hash_password


def crear_administrador():
    db = SessionLocal()

    try:
        print("CREACION DEL ADMINISTRADOR INICIAL")

        nombre = input("Nombre: ").strip()
        email = input("Correo electronico: ").strip().lower()

        if not nombre or not email:
            print("El nombre y el correo son obligatorios.")
            return

        existente = db.query(Usuario).filter(
            Usuario.email == email
        ).first()

        if existente:
            print("Ya existe un usuario con ese correo.")
            return

        password = getpass("Contrasena: ")
        confirmacion = getpass("Confirmar contrasena: ")

        if password != confirmacion:
            print("Las contrasenas no coinciden.")
            return

        if len(password) < 8:
            print("La contrasena debe tener al menos 8 caracteres.")
            return

        administrador = Usuario(
            nombre=nombre,
            email=email,
            password_hash=generar_hash_password(password),
            rol="admin"
        )

        db.add(administrador)
        db.commit()

        print("Administrador creado con éxito.")

    except Exception:
        db.rollback()
        print("No se pudo crear el administrador.")
        raise

    finally:
        db.close()


if __name__ == "__main__":
    crear_administrador()
