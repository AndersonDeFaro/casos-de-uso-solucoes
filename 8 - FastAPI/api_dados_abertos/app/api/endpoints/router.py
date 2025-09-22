# app/api/endpoints/router.py

from fastapi import APIRouter
# Importe os routers do subdiretório 'system_a'
from .system_a.users import router as users_router
from .system_a.products import router as products_router

# Se você também tiver routers para deputado_federal, importe-os também
#from .deputado_federal.router import router as deputado_federal_router

# Cria a instância principal do roteador para este módulo
api_router = APIRouter()

# Inclui os roteadores, especificando seus prefixos de URL e tags
api_router.include_router(users_router, prefix="/users", tags=["Users"])
api_router.include_router(products_router, prefix="/products", tags=["Products"])

# Exemplo de como incluir o router para deputado_federal
#api_router.include_router(deputado_federal_router, prefix="/deputados", tags=["Deputados"])