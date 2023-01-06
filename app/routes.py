from fastapi import APIRouter

from app.controllers.common import router as common_router

api_router = APIRouter()


api_router.include_router(common_router, tags=["Common"])
