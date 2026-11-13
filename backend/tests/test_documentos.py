import os

os.environ["TESTING"] = "1"

os.environ["DATABASE_URL"] = "sqlite://"

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, JSON
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy.dialects.postgresql import JSONB

from app.database import Base, get_db, engine as engine_aplicacion
from app.auth import obtener_usuario_actual
from app.models import Usuario, Plantilla, DocumentoGenerado
from main import app

if engine_aplicacion.dialect.name != "sqlite":
    raise RuntimeError(
        "Pruebas canceladas: la base de datos no es SQLite."
    )

engine_pruebas = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SessionPruebas = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_pruebas,
)

def configurar_tablas_prueba():
    for tabla in Base.metadata.tables.values():
        for columna in tabla.columns:
            if isinstance(columna.type, JSONB):
                columna.type = JSONB().with_variant(JSON(), "sqlite")

def obtener_db_prueba():
    db = SessionPruebas()
    try:
        yield db
    finally:
        db.close()

def crear_usuario_prueba(db, nombre, email):
    usuario = Usuario(
        nombre=nombre,
        email=email,
        password_hash="hash_ficticio_para_pruebas",
        rol="usuario",
        activo=True
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario

def crear_documento_prueba(db, usuario_id, version=1):
    plantilla = Plantilla(
        titulo="Plantilla de prueba",
        cuerpo_base="Contenido base para pruebas"
    )

    db.add(plantilla)
    db.flush()

    documento = DocumentoGenerado(
        plantilla_id=plantilla.id,
        usuario_id=usuario_id,
        contenido="Documento original de prueba",
        datos_variables={"nombre_empleado": "Empleado de Prueba"},
        estado="confirmado",
        version=version
    )

    db.add(documento)
    db.commit()
    db.refresh(documento)

    return documento

@pytest.fixture
def cliente_prueba():
    configurar_tablas_prueba()

    Base.metadata.create_all(bind=engine_pruebas)

    app.dependency_overrides[get_db] = obtener_db_prueba

    try:
        cliente = TestClient(app)
        yield cliente

    finally:
        app.dependency_overrides.clear()
        Base.metadata.drop_all(bind=engine_pruebas)


def test_editar_documento_sin_token(cliente_prueba):
    respuesta = cliente_prueba.put(
        "/documentos/1/editar",
        json={
            "contenido": "Documento de prueba",
            "datos_variables": None,
            "version_actual": 1
        }
    )

    assert respuesta.status_code == 401

def test_usuario_no_puede_editar_documento_ajeno(cliente_prueba):
    db = SessionPruebas()

    try:
        propietario = crear_usuario_prueba(
            db, "Usuario Propietario", "propietario@prueba.local"
        )

        otro_usuario = crear_usuario_prueba(
            db, "Usuario Diferente", "otro@prueba.local"
        )

        documento = crear_documento_prueba(
            db, propietario.id
        )

        app.dependency_overrides[obtener_usuario_actual] = (
            lambda: otro_usuario
        )

        respuesta = cliente_prueba.put(
            f"/documentos/{documento.id}/editar",
            json={
                "contenido": "Intento de edición no autorizado",
                "datos_variables": None,
                "version_actual": 1
            }
        )

        assert respuesta.status_code == 403

    finally:
        app.dependency_overrides.pop(obtener_usuario_actual, None)
        db.close()

def test_editar_documento_con_version_antigua(cliente_prueba):
    db = SessionPruebas()

    try:
        propietario = crear_usuario_prueba(
            db, "Usuario Versiones", "versiones@prueba.local"
        )

        documento = crear_documento_prueba(
            db, propietario.id, version=2
        )

        app.dependency_overrides[obtener_usuario_actual] = (
            lambda: propietario
        )

        respuesta = cliente_prueba.put(
            f"/documentos/{documento.id}/editar",
            json={
                "contenido": "Intento con versión antigua",
                "datos_variables": None,
                "version_actual": 1
            }
        )

        assert respuesta.status_code == 409

    finally:
        app.dependency_overrides.pop(obtener_usuario_actual, None)
        db.close()