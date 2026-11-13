from sqlalchemy import text
from app.database import engine, Base, SessionLocal
from app.models import (
    Plantilla,
    DocumentoGenerado,
    Usuario,
    TokenRecuperacion,
    VersionDocumento,
)
from app.plantillas import plantillas


def resetear_base_datos():
    print("ADVERTENCIA: Esta operación eliminará datos de la base de datos.")
    print("Se borrarán documentos, versiones, usuarios y plantillas.")

    confirmacion = input(
        "Escribe RESETEAR para confirmar: "
    ).strip()

    if confirmacion != "RESETEAR":
        print("Operación cancelada.")
        return

    print("1. Eliminando tablas antiguas...")

    with engine.begin() as conn:
        conn.execute(text("""
            DROP TABLE IF EXISTS
                versiones_documentos,
                tokens_recuperacion,
                documentos_generados,
                documentos,
                usuarios,
                plantillas
            CASCADE;
        """))

    print("2. Recreando tablas...")

    Base.metadata.create_all(bind=engine)

    print("3. Registrando las cinco plantillas...")

    db = SessionLocal()

    try:
        plantillas(db)
        print("Base de datos reiniciada correctamente.")

    except Exception:
        db.rollback()
        print("Error al registrar las plantillas.")
        raise

    finally:
        db.close()

if __name__ == "__main__":
    resetear_base_datos()