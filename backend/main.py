import base64
import traceback
from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Dict, Any, Optional

from app.database import engine, Base, get_db
from app.models import Plantilla, DocumentoGenerado
from app.services_ai import generar_redaccion_legal
from app.services_export import exportar_a_pdf, exportar_a_docx

# Crear tablas en PostgreSQL
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Notificaciones Legales")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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


@app.get("/plantillas/")
def listar_plantillas(db: Session = Depends(get_db)):
    try:
        # 1. Eliminar la versión antigua duplicada sin tildes si existe
        duplicado_antiguo = db.query(Plantilla).filter(Plantilla.titulo == "Notificacion de Rescision Laboral").first()
        if duplicado_antiguo:
            db.delete(duplicado_antiguo)
            db.commit()

        # 2. Catálogo oficial de las 5 plantillas base
        plantillas_catalog = [
            {
                "titulo": "Notificación de Rescisión Laboral",
                "cuerpo_base": "[empresa_nombre]\n\nSr.(a) [nombre_empleado]\nPresente.-\n\nPor medio de la presente se le notifica formalmente la rescisión de su contrato laboral con fecha efectiva al [fecha_efectiva], derivado de: [motivo].\n\nAtentamente,\n[firmante_nombre]\n[firmante_cargo]"
            },
            {
                "titulo": "Acta Administrativa por Incumplimiento",
                "cuerpo_base": "[empresa_nombre]\n\nACTA ADMINISTRATIVA DE HECHOS\n\nEn la ciudad de Ecatepec, Estado de México, con fecha [fecha_efectiva], se levanta la presente Acta Administrativa al empleado(a) [nombre_empleado].\n\nHECHOS:\nSe deja constancia del incumplimiento relativo a: [motivo].\n\nEl presente documento se integra a su expediente laboral para los efectos legales a que haya lugar.\n\nAtentamente,\n[firmante_nombre]\n[firmante_cargo]"
            },
            {
                "titulo": "Carta de Recomendación Laboral",
                "cuerpo_base": "[empresa_nombre]\n\nA QUIEN CORRESPONDA:\n\nPor medio de la presente hago constar que el(la) C. [nombre_empleado] laboró en esta institución con fecha de término al [fecha_efectiva], desempeñando sus actividades con responsabilidad y profesionalismo.\n\nEl motivo de conclusión de la relación laboral fue: [motivo].\n\nSe extiende la presente para los fines que al interesado convengan.\n\nAtentamente,\n[firmante_nombre]\n[firmante_cargo]"
            },
            {
                "titulo": "Convenio de Confidencialidad (NDA)",
                "cuerpo_base": "[empresa_nombre]\n\nACUERDO DE CONFIDENCIALIDAD Y NO DIVULGACIÓN\n\nEntre [empresa_nombre] y el(la) C. [nombre_empleado], con fecha efectiva al [fecha_efectiva].\n\nOBJETO Y ALCANCE:\nEl receptor se compromete a mantener estricta confidencialidad respecto a la información técnica, comercial y operativa recibida, en particular sobre: [motivo].\n\nAtentamente,\n[firmante_nombre]\n[firmante_cargo]"
            },
            {
                "titulo": "Aviso de Suspensión Temporal de Labores",
                "cuerpo_base": "[empresa_nombre]\n\nSr.(a) [nombre_empleado]\nPresente.-\n\nPor medio del presente comunicado se le informa la suspensión temporal de sus actividades laborales con fecha efectiva al [fecha_efectiva].\n\nDicha medida responde a: [motivo].\n\nAtentamente,\n[firmante_nombre]\n[firmante_cargo]"
            }
        ]

        # 3. Sincronizar e insertar cualquier plantilla faltante
        for p_data in plantillas_catalog:
            existe = db.query(Plantilla).filter(Plantilla.titulo == p_data["titulo"]).first()
            if not existe:
                nueva_plantilla = Plantilla(
                    titulo=p_data["titulo"],
                    cuerpo_base=p_data["cuerpo_base"]
                )
                db.add(nueva_plantilla)
        
        db.commit()

        # Retornar las plantillas ordenadas por ID
        return db.query(Plantilla).order_by(Plantilla.id.asc()).all()

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al listar plantillas: {str(e)}")


@app.post("/documentos/redactar-borrador/")
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
def guardar_documento(solicitud: SolicitudGuardar, db: Session = Depends(get_db)):
    plantilla = db.query(Plantilla).filter(Plantilla.id == solicitud.plantilla_id).first()
    if not plantilla:
        raise HTTPException(status_code=404, detail="Plantilla no encontrada")

    doc = DocumentoGenerado(
        plantilla_id=plantilla.id,
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


@app.get("/documentos/")
def listar_documentos(db: Session = Depends(get_db)):
    docs = db.query(DocumentoGenerado).order_by(DocumentoGenerado.id.desc()).all()
    resultado = []
    for d in docs:
        resultado.append({
            "documento_id": d.id,
            "plantilla_id": d.plantilla_id,
            "titulo_plantilla": d.plantilla.titulo if d.plantilla else "Carta Legal",
            "estado": d.estado,
            "version": d.version,
            "contenido": d.contenido
        })
    return resultado


@app.post("/documentos/{documento_id}/exportar/pdf")
async def exportar_pdf_con_logo(
    documento_id: int, 
    logo_pos: str = Form("ninguno"),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    doc = db.query(DocumentoGenerado).filter(DocumentoGenerado.id == documento_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
        
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
    db: Session = Depends(get_db)
):
    doc = db.query(DocumentoGenerado).filter(DocumentoGenerado.id == documento_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento no encontrado")
        
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