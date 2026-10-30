from app.models import Plantilla

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

def plantillas(db):
    """
    Registra únicamente las plantillas que todavía
    no existen en PostgreSQL.

    No modifica ni elimina plantillas existentes.
    """

    nuevas = 0

    for datos in plantillas_catalog:
        existente = (
            db.query(Plantilla)
            .filter(Plantilla.titulo == datos["titulo"])
            .first()
        )

        if existente is None:
            plantilla = Plantilla(
                titulo=datos["titulo"],
                cuerpo_base=datos["cuerpo_base"]
            )

            db.add(plantilla)
            nuevas += 1

    if nuevas > 0:
        db.commit()

    return nuevas
