from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.core.config import settings
from app.api.endpoints.router import api_router

# --- Importações corrigidas ---
# Importa as funções de gerenciamento de sessão do PostgreSQL
from app.db.postgres.session import create_tables
# Importa as funções de gerenciamento de sessão assíncrona do MongoDB
from app.db.mongodb.session import connect_to_mongo_async, close_mongo_async_connection
# --- Fim das importações corrigidas ---


# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gerencia o ciclo de vida da aplicação
    """
    # Startup
    logger.info("Iniciando aplicação...")
    
    # Criar tabelas do PostgreSQL
    create_tables()
    logger.info("Tabelas PostgreSQL criadas/verificadas")
    
    # Conectar ao MongoDB de forma assíncrona
    try:
        await connect_to_mongo_async()
        logger.info("Conexão assíncrona com MongoDB estabelecida.")
        
        logger.info("Aplicação iniciada com sucesso")
        yield
    finally:
        # Shutdown
        logger.info("Encerrando aplicação...")
        await close_mongo_async_connection()
        logger.info("Conexão assíncrona com MongoDB fechada.")
        logger.info("Aplicação encerrada")

# Criar instância do FastAPI no nível superior do arquivo
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    description="API com PostgreSQL e MongoDB",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.is_development else [
        "http://localhost:3000",
        "https://yourdomain.com",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(api_router, prefix="/api/v1")

# Health check
@app.get("/health")
async def health_check():
    """Endpoint para verificar a saúde da aplicação"""
    return {
        "status": "healthy",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.environment
    }

@app.get("/")
async def root():
    """Endpoint raiz"""
    return {
        "message": f"Bem-vindo ao {settings.app_name}",
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level="info" if settings.is_production else "debug"
    )
