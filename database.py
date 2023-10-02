from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.environ.get("DB_URL")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_recycle=500,
    pool_size=5,
    max_overflow=20,
    echo=False,
    echo_pool=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()