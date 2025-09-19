from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
from app.core.config import settings

# Conexão com o PostgreSQL
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Conexão com o MongoDB
client = MongoClient(settings.MONGO_URL)
db = client[settings.MONGO_DB]


def get_db() -> Generator:
    """
    Cria uma sessão de banco de dados para o PostgreSQL e a fecha automaticamente.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def get_mongo_db():
    """
    Retorna o cliente do MongoDB.
    """
    return db