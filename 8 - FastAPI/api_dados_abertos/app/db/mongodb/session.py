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
    # Usa a URL completa gerada pela classe Settings
    client = MongoClient(settings.mongo_url)
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
        return client[settings.mongo_db]
    else:
        raise Exception("Conexão com o MongoDB não estabelecida.")

# --- Funções para a conexão ASSÍNCRONA com o MongoDB (Recomendado para FastAPI) ---
async def connect_to_mongo_async():
    """Conecta ao MongoDB de forma assíncrona."""
    global async_client
    # Aumenta o tempo limite de seleção do servidor para 5 segundos
    # e usa a URL completa para a conexão
    async_client = AsyncIOMotorClient(settings.mongo_url, serverSelectionTimeoutMS=5000)
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
        return async_client[settings.mongo_db]
    else:
        raise Exception("Conexão assíncrona com o MongoDB não estabelecida.")
