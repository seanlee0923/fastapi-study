from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from dotenv import load_dotenv
import os

load_dotenv()
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("DB")
host = os.getenv("MYSQL_HOST")
port = os.getenv("MYSQL_PORT")



SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()