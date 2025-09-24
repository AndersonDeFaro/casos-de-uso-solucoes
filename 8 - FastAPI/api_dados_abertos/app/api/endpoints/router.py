from fastapi import APIRouter
from .users_api.router import router as users_api_router
from .deputado_federal.router import router as deputado_federal_router

# Cria a instância principal do roteador para este módulo
api_router = APIRouter()
# Inclui os roteadores
api_router.include_router(users_api_router)
api_router.include_router(deputado_federal_router)