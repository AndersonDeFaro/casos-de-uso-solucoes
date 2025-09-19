from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from typing import Generator, Optional
import logging

from app.core.config import settings
from app.db.base import SessionLocal, mongodb, mongo_sync_client

logger = logging.getLogger(__name__)

# PostgreSQL Session
def get_db() -> Generator[Session, None, None]:
    """
    Dependency que retorna uma sessão do PostgreSQL
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# MongoDB Async Connection
async def connect_to_mongo():
    """Conecta ao MongoDB"""
    try:
        mongodb.client = AsyncIOMotorClient(
            settings.mongo_url,
            maxPoolSize=10,
            minPoolSize=5,
        )
        mongodb.database = mongodb.client[settings.mongo_db]
        
        # Testa a conexão
        await mongodb.client.admin.command('ping')
        logger.info("Conectado ao MongoDB com sucesso")
        
    except Exception as e:
        logger.error(f"Erro ao conectar ao MongoDB: {e}")
        raise

async def close_mongo_connection():
    """Fecha a conexão com o MongoDB"""
    if mongodb.client:
        mongodb.client.close()
        logger.info("Conexão com MongoDB fechada")

def get_mongo_db() -> AsyncIOMotorDatabase:
    """
    Dependency que retorna o database do MongoDB
    """
    if not mongodb.database:
        raise RuntimeError("MongoDB não está conectado")
    return mongodb.database

# MongoDB Sync Connection (para operações síncronas se necessário)
def connect_to_mongo_sync():
    """Conecta ao MongoDB de forma síncrona"""
    global mongo_sync_client
    try:
        mongo_sync_client = pymongo.MongoClient(
            settings.mongo_url,
            maxPoolSize=10,
            minPoolSize=5,
        )
        # Testa a conexão
        mongo_sync_client.admin.command('ping')
        logger.info("Conectado ao MongoDB (sync) com sucesso")
        
    except Exception as e:
        logger.error(f"Erro ao conectar ao MongoDB (sync): {e}")
        raise

def close_mongo_sync_connection():
    """Fecha a conexão síncrona com o MongoDB"""
    global mongo_sync_client
    if mongo_sync_client:
        mongo_sync_client.close()
        logger.info("Conexão síncrona com MongoDB fechada")

def get_mongo_sync_db():
    """
    Retorna o database do MongoDB de forma síncrona
    """
    if not mongo_sync_client:
        raise RuntimeError("MongoDB sync não está conectado")
    return mongo_sync_client[settings.mongo_db]
