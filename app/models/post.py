from sqlalchemy import Column, Integer, String, DateTime
from app.db.database import Base

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime)
    user_id = Column(Integer, nullable=False)