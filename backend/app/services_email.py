
import os
import smtplib
import ssl

from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()


def enviar_correo(destinatario: str, asunto: str, contenido: str):
    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    smtp_from = os.getenv("SMTP_FROM_EMAIL")
    smtp_use_tls = os.getenv("SMTP_USE_TLS", "true").lower() == "true"

    if not all([smtp_host, smtp_user, smtp_password, smtp_from]):
        raise RuntimeError(
            "La configuración SMTP está incompleta."
        )

    mensaje = EmailMessage()
    mensaje["From"] = smtp_from
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.set_content(contenido)

    contexto_ssl = ssl.create_default_context()

    with smtplib.SMTP(
        smtp_host,
        smtp_port,
        timeout=15
    ) as servidor:
        servidor.ehlo()

        if smtp_use_tls:
            servidor.starttls(context=contexto_ssl)
            servidor.ehlo()

        servidor.login(smtp_user, smtp_password)
        servidor.send_message(mensaje)
