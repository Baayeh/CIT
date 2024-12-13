import logging
from datetime import datetime, timedelta
from uuid import uuid4

import jwt
from passlib.context import CryptContext

from app.core.config import get_settings

settings = get_settings()

password_context = CryptContext(schemes=["bcrypt"])

ACCESS_TOKEN_EXPIRY = 3600  # one hour in seconds


def generate_passwd_hash(password: str) -> str:
    """hash user password"""
    hash = password_context.hash(password)

    return hash


def verify_passwd(password: str, hash: str) -> bool:
    """Verify user password"""
    return password_context.verify(password, hash)


def create_access_token(
    user_data: dict, expiry: timedelta = None, refresh: bool = False
):
    """Create access token"""

    payload = {}
    payload["user"] = user_data
    payload["exp"] = datetime.now() + (
        expiry if expiry is not None else timedelta(seconds=ACCESS_TOKEN_EXPIRY)
    )
    payload["jti"] = str(uuid4())

    payload["refresh"] = refresh

    token = jwt.encode(
        payload=payload, key=settings.JWT.secret, algorithm=settings.JWT.algo
    )

    return token


def decode_token(token: str) -> dict:
    try:
        token_data = jwt.decode(
            jwt=token, key=settings.JWT.secret, algorithms=[settings.JWT.algo]
        )
        return token_data
    except jwt.PyJWKError as e:
        logging.exception(e)
        return None
