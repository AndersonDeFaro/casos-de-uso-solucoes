# Arquivo: app/db/postgres/session.py
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Importa as configurações globais da sua aplicação
from app.core.config import settings

# --- Conexão e Motor do PostgreSQL ---
# O 'pool_pre_ping' garante que a conexão está ativa antes de ser usada
engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Funções de Utilitário para o PostgreSQL ---

def get_db() -> Generator[Session, None, None]:
    """
    Cria uma sessão de banco de dados para o PostgreSQL e a fecha automaticamente.
    Esta é uma dependência injetável para rotas do FastAPI.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_tables():
    """
    Cria todas as tabelas no banco de dados.
    Importe esta função no seu main.py ou em um script para inicializar o DB.
    """
    # A base precisa ser importada para que a metadados seja conhecida
    from app.db.postgres.base import Base
    Base.metadata.create_all(bind=engine)
# Arquivo: app/db/mongodb/session.py
from pymongo import MongoClient
from motor.motor_asyncio import AsyncIOMotorClient

# Importa as configurações globais da sua aplicação
from app.core.config import settings

# Variáveis globais para os clientes de banco de dados
client = None
async_client = None

# --- Funções para a conexão SÍNCRONA com o MongoDB ---
def connect_to_mongo_sync():
    """Conecta ao MongoDB de forma síncrona."""
    global client
    client = MongoClient(settings.mongo_db)
    print("Conexão síncrona com MongoDB estabelecida.")

def close_mongo_sync_connection():
    """Fecha a conexão síncrona com o MongoDB."""
    global client
    if client:
        client.close()
        print("Conexão síncrona com MongoDB fechada.")

def get_mongo_db():
    """Retorna o cliente do MongoDB síncrono.
    Isso é uma dependência injetável para rotas que usam MongoDB.
    """
    if client:
        return client[settings.mongo_db_name]
    else:
        raise Exception("Conexão com o MongoDB não estabelecida.")

# --- Funções para a conexão ASSÍNCRONA com o MongoDB (Recomendado para FastAPI) ---
async def connect_to_mongo_async():
    """Conecta ao MongoDB de forma assíncrona."""
    global async_client
    async_client = AsyncIOMotorClient(settings.mongo_db, serverSelectionTimeoutMS=2000)
    print("Conexão assíncrona com MongoDB estabelecida.")

async def close_mongo_async_connection():
    """Fecha a conexão assíncrona com o MongoDB."""
    global async_client
    if async_client:
        async_client.close()
        print("Conexão assíncrona com MongoDB fechada.")

async def get_async_mongo_db():
    """Retorna o cliente assíncrono do MongoDB.
    Isso é uma dependência injetável para rotas que usam MongoDB assíncrono.
    """
    if async_client:
        return async_client[settings.mongo_db_name]
    else:
        raise Exception("Conexão assíncrona com o MongoDB não estabelecida.")
