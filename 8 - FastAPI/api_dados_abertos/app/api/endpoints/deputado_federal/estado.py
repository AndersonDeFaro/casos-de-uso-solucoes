from fastapi import APIRouter, Depends
from typing import Collection
from app.db.mongodb.session import get_async_mongo_db as get_mongo_db


router = APIRouter()

@router.get("/{sigla_uf}")
def read_sigla_uf(sigla_uf: str, mongo_db: Collection = Depends(get_mongo_db)):
    """
    Endpoint para buscar informações de deputados por estado.
    """
    # Lógica de busca no banco de dados
    # Por exemplo:
    # return list(mongo_db["deputados"].find({"sigla_uf": sigla_uf}))
    return {"message": f"Endpoint for sigla_uf: {sigla_uf}"}
