from fastapi import APIRouter
from api.endpoints import adminApi
from api.endpoints import cookApi
from api.endpoints import loginApi
from api.endpoints import noticeApi
from api.endpoints import profilesApi
from api.endpoints import waiterApi

api_router = APIRouter()
api_router.include_router(adminApi.router)
api_router.include_router(cookApi.router)
api_router.include_router(loginApi.router)
api_router.include_router(noticeApi.router)
api_router.include_router(profilesApi.router)
api_router.include_router(waiterApi.router)
