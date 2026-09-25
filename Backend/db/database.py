from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import Settings
from Backend.core.config import Settings
engine = create_engine(Settings.DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

def get_db():
    db =sessionmaker()
    try:
        yield db
    finally:
        db.close()

def crete_tables():
    Base.metadata.create_all(bind=engine)