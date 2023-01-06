from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from redis import Redis
import uuid

from app.core.config import settings
from app.serializers.common import DefaultResponse
from app.db.deps import get_db
from app.redis.redis import redis_conn

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
def root() -> dict:
    return {
        "status": True,
        "msg": "Project information",
        "details": {
            "name": f"{settings.PROJECT_NAME}",
            "version": f"{settings.APP_VERSION}",
        },
    }


@router.get("/health", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def get_db_health(db: AsyncSession = Depends(get_db)) -> dict:
    try:
        healthy = await db.execute("SELECT 1")
        if healthy.scalars().first() is None:
            raise HTTPException(status_code=404, detail={"msg": "Not Healthy ❌"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": True, "msg": "Healthy ✅"}

@router.get("/redis", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def get_redis_health() -> dict:
    try:
        healthy = redis_conn.ping()
        if not healthy:
            raise HTTPException(status_code=404, detail={"msg": "Not Healthy ❌"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": True, "msg": "Healthy ✅"}


@router.get("/test-redis-write", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def write_redis() -> dict:
    dict_to_write = {}
    offset = 0
    for i in range(100):
        for id in range(10_000):
            dict_to_write[str(id + offset)] = str(uuid.uuid4())
        redis_conn.multi_set(dict_to_write)
        dict_to_write = {}
        offset += 10_000

    return {"status": True, "msg": "Done ✅"}

@router.get("/test-redis-read", status_code=status.HTTP_200_OK, response_model=DefaultResponse)
async def read_redis() -> dict:
    
    items = []
    offset = 0
    for i in range(100):
        items_to_read = [str(id) for id in range(offset, 10_000 + offset)]
        items.extend(redis_conn.multi_get(items_to_read))
        offset += 10_000

    return {"status": True, "msg": "Done ✅", "details": {"items": len(items)}}
