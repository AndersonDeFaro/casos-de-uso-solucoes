from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from motor.motor_asyncio import AsyncIOMotorClient
import pymongo
from typing import Optional

from app.core.config import settings

# PostgreSQL Setup
engine = create_engine(
    settings.database_url,
    echo=settings.debug,  # Log SQL queries em desenvolvimento
    pool_pre_ping=True,
    pool_recycle=300,
)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

Base = declarative_base()

# Metadata para migrations
metadata = MetaData()

# MongoDB Setup
class MongoDB:
    client: Optional[AsyncIOMotorClient] = None
    database = None

# Instância global do MongoDB
mongodb = MongoDB()

# Cliente síncrono do MongoDB para operações que não precisam ser async
mongo_sync_client: Optional[pymongo.MongoClient] = None