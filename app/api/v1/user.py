import http

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.schemas import user as schema

from app.crud import user as crud
from app.db.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("/sign-up")
def sign_up(user: schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=http.HTTPStatus.CONFLICT, detail="Username already exists")

    return crud.create_user(db,user)


@router.get("/sign-in", response_model=None)
def sign_in(user: schema.UserLogin, db: Session = Depends(get_db)):
    existing_user = crud.get_user_by_username(db,user.username)
    if not existing_user:
        raise HTTPException(status_code=http.HTTPStatus.CONFLICT, detail="Wrong username or password")

    login_result = crud.login_user(existing_user, user.password)
    if not login_result.Status:
        raise HTTPException(status_code=http.HTTPStatus.CONFLICT, detail="Wrong username or password")

    return {"result": True, "token": login_result.access_token}
