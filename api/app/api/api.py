
from fastapi import APIRouter
from api.endpoints import subscriptions
from api.endpoints import login


api_router = APIRouter()
api_router.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])
api_router.include_router(login.router, prefix="/login", tags=["login"])
