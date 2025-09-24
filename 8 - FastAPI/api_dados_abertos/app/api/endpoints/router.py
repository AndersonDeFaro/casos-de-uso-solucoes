from fastapi import APIRouter
# Importe os routers do subdiretório 'system_a'
from .system_a.router import router as system_a_router

# Importe o router do subdiretório 'deputado_federal'
from .deputado_federal.router import router as deputado_federal_router

# Cria a instância principal do roteador para este módulo
api_router = APIRouter()

# Inclui os roteadores, especificando seus prefixos de URL e tags
api_router.include_router(system_a_router)

# Exemplo de como incluir o router para deputado_federal
api_router.include_router(deputado_federal_router)