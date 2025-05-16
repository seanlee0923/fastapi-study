from fastapi import APIRouter
from app.api.v1 import user, post

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(post.router)