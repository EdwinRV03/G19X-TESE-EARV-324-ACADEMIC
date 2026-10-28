from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Plantilla(Base):
    __tablename__ = "plantillas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    cuerpo_base = Column(Text, nullable=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    documentos = relationship("DocumentoGenerado", back_populates="plantilla")


class DocumentoGenerado(Base):
    __tablename__ = "documentos_generados"

    id = Column(Integer, primary_key=True, index=True)
    plantilla_id = Column(Integer, ForeignKey("plantillas.id"), nullable=False)
    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=True
    )
    contenido = Column(Text, nullable=False)
    estado = Column(String(50), default="confirmado")
    version = Column(Integer, default=1)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    plantilla = relationship("Plantilla", back_populates="documentos")
    usuario = relationship("Usuario", back_populates="documentos")


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=True)
    activo = Column(Boolean, nullable=False, default=True)
    documentos = relationship("DocumentoGenerado", back_populates="usuario")

class TokenRecuperacion(Base):
    __tablename__ = "tokens_recuperacion"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(
        Integer,
        ForeignKey("usuarios.id"),
        nullable=False
    )

    token_hash = Column(String(64), nullable=False, unique=True)

    fecha_expiracion = Column(DateTime, nullable=False)

    utilizado = Column(
        Boolean,
        nullable=False,
        default=False
    )
