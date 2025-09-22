from fastapi import APIRouter
# Importa o router do arquivo estado.py, que está na mesma pasta.
from .estado import router as estado_router

router = APIRouter(tags=["Deputados Federais"])

# Inclui o router importado, definindo um prefixo para as rotas.
# O prefixo é a parte da URL que vem depois do "deputados", por exemplo: /api/v1/deputados/estado/{sigla}
router.include_router(estado_router)