
import os
import hashlib
import hmac
from datetime import datetime, timedelta, timezone

import jwt
from jwt import InvalidTokenError
from argon2 import PasswordHasher
from argon2.exceptions import (
    VerifyMismatchError,
    VerificationError,
    InvalidHashError,
)
from dotenv import load_dotenv

load_dotenv()

password_hasher = PasswordHasher()

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_MINUTES = int(
    os.getenv("JWT_ACCESS_TOKEN_MINUTES", "30")
)

if not JWT_SECRET_KEY or len(JWT_SECRET_KEY) < 32:
    raise RuntimeError(
        "JWT_SECRET_KEY no está configurada correctamente"
    )


def generar_hash_password(password: str) -> str:
    """Genera un hash seguro de la contraseña."""
    return password_hasher.hash(password)


def verificar_password(password: str, password_hash: str) -> bool:
    """Comprueba si la contraseña coincide con su hash."""
    try:
        return password_hasher.verify(password_hash, password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False

def crear_token_acceso(usuario_id: int, password_hash: str):
    ahora = datetime.now(timezone.utc)

    payload = {
        "sub": str(usuario_id),
        "iat": ahora,
        "exp": ahora + timedelta(
            minutes=JWT_ACCESS_TOKEN_MINUTES
        ),
        "pwdv": generar_version_password(password_hash)
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )

def verificar_token_acceso(token: str) -> int | None:
    """Valida el token y devuelve el identificador del usuario."""

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
            options={"require": ["sub", "iat", "exp"]},
        )

        usuario_id = int(payload["sub"])

        if usuario_id <= 0:
            return None

        return usuario_id

    except (InvalidTokenError, ValueError, TypeError):
        return None

def generar_version_password(password_hash: str) -> str:
    return hmac.new(
        JWT_SECRET_KEY.encode("utf-8"),
        password_hash.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

def verificar_version_token(token: str, password_hash: str) -> bool:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM],
            options={"require": ["sub", "iat", "exp", "pwdv"]}
        )

        version_token = payload.get("pwdv")

        if not isinstance(version_token, str):
            return False

        version_actual = generar_version_password(password_hash)

        return hmac.compare_digest(version_token, version_actual)

    except (InvalidTokenError, ValueError, TypeError):
        return False
