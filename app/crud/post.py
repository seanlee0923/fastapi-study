from sqlalchemy.orm import Session
from app.models.post import Post
from app.schemas.post import PostCreate

def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()

def get_post_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).first()