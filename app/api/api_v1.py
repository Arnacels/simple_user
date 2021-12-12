from fastapi import APIRouter

import user

api_router = APIRouter()

api_router.include_router(user.router, prefix="/users", tags=["user"])
