from fastapi import APIRouter, Depends, HTTPException
from typing import List
import json
from bson import json_util
from motor.motor_asyncio import AsyncIOMotorClient

# Importa as dependências de banco de dados
from app.db.mongodb.session import get_async_mongo_db as get_mongo_db

router = APIRouter()

@router.get(
    "/estado/{sigla_uf}",
    summary="Busca deputados federais por estado",
    response_description="Lista de deputados federais de um estado específico."
)
async def read_deputados_por_estado(
    sigla_uf: str,
    mongo_db = Depends(get_mongo_db)
):
    """
    **Busca deputados federais de um estado específico.**
    
    - **sigla_uf**: Sigla do estado (ex: "AP").
    
    A busca não diferencia maiúsculas e minúsculas e retorna uma lista de deputados.
    """
    # Acessa a coleção "deputados"
    deputados_collection = mongo_db["deputados"]
    
    # Prepara a consulta para buscar por 'siglaUf' (não diferencia maiúsculas/minúsculas)
    # A query foi ajustada para remover as âncoras ^ e $ para garantir que a busca encontre os resultados
    # mesmo que haja espaços ou outros caracteres extras na string.
    query = {"siglaUf": {"$regex": f"{sigla_uf}", "$options": "i"}}
    
    # Executa a busca assíncrona
    deputados_cursor = deputados_collection.find(query)
    
    # Converte o cursor para uma lista
    deputados = await deputados_cursor.to_list(length=100)
    
    if not deputados:
        raise HTTPException(status_code=404, detail="Nenhum deputado encontrado para o estado fornecido.")
    
    # Serializa os documentos para JSON, convertendo o ObjectId para string
    deputados_json = json.loads(json_util.dumps(deputados))
    
    return deputados_json
