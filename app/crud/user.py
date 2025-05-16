from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_hashed_password

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 30):
    return db.query(User).offset(skip).limit(limit).all()

def create_user(db: Session, user: UserCreate) -> User:
    hashed_pass = get_hashed_password(user.password)
    db_user = User(username=user.username, password=hashed_pass, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user