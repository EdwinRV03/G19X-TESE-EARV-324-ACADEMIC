# -*- coding: utf-8 -*-
from app.database import engine, Base, SessionLocal
from app.models import Plantilla, DocumentoGenerado
from sqlalchemy import text

print("1. Eliminando tablas antiguas en cascada...")
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS documentos_generados, documentos, plantillas CASCADE;"))
    conn.commit()

print("2. Recreando estructura de tablas en PostgreSQL...")
Base.metadata.create_all(bind=engine)

print("3. Insertando plantilla base...")
db = SessionLocal()
plantilla_defecto = Plantilla(
    titulo="Notificacion de Rescision Laboral",
    cuerpo_base=(
        "[empresa_nombre]\n\n"
        "Sr.(a) [nombre_empleado]\n"
        "Presente.-\n\n"
        "Por medio de la presente se le notifica formalmente la rescision de su "
        "contrato laboral con fecha efectiva al [fecha_efectiva], derivado de: [motivo].\n\n"
        "Atentamente,\n"
        "[firmante_nombre]\n"
        "[firmante_cargo]"
    )
)
db.add(plantilla_defecto)
db.commit()

print("Base de datos reseteada y lista con exito!")
