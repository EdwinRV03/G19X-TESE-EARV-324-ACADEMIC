import hashlib
import secrets

from datetime import datetime, timedelta, timezone


MINUTOS_RECUPERACION = 15


def generar_token_recuperacion():
    token = secrets.token_urlsafe(32)

    token_hash = hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()

    fecha_expiracion = (
        datetime.now(timezone.utc)
        + timedelta(minutes=MINUTOS_RECUPERACION)
    )

    return token, token_hash, fecha_expiracion.replace(tzinfo=None)


def calcular_hash_token(token: str) -> str:
    return hashlib.sha256(
        token.encode("utf-8")
    ).hexdigest()


def token_esta_vigente(fecha_expiracion: datetime) -> bool:
    ahora = datetime.now(timezone.utc)

    if fecha_expiracion.tzinfo is None:
        fecha_expiracion = fecha_expiracion.replace(tzinfo=timezone.utc)

    return ahora < fecha_expiracion
