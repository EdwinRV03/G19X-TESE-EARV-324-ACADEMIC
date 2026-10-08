from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, JSON
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
    contenido = Column(Text, nullable=False)
    estado = Column(String(50), default="confirmado")
    version = Column(Integer, default=1)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    plantilla = relationship("Plantilla", back_populates="documentos")