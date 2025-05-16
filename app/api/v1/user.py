import http

from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.schemas import user as schema

from app.crud import user as crud
from app.db.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/sign-in")
def sign_in(user: schema.UserCreate, db: Session = get_db):
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=http.HTTPStatus.CONFLICT, detail="Username already exists")

    return crud.create_user(db,user)


@router.get("/sign-up")
def sign_up():
    print("up")