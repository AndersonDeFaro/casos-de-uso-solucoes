from fastapi import APIRouter
# Importa o router do arquivo estado.py, que está na mesma pasta.
from . import estado

router = APIRouter(prefix="/deputado_federal", tags=["Deputados Federais"])

router.include_router(estado.router)