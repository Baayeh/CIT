import aioredis

from app.core.config import get_settings

settings = get_settings()

JTI_EXPIRY_TIME = 3600  # one hour in seconds

token_blocklist = aioredis.StrictRedis(
    host=settings.REDIS.host, port=settings.REDIS.port, db=0
)


async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(name=jti, value="", exp=JTI_EXPIRY_TIME)


async def token_in_blocklist(jti: str) -> bool:
    jti_str = await token_blocklist.get(jti)

    return jti_str is not None
