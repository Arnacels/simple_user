from fastapi import APIRouter

import user, logs

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["user"])
api_router.include_router(logs.router, prefix="/logs", tags=["logs"])
