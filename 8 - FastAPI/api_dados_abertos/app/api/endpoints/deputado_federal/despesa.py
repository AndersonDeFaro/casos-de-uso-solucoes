from fastapi import APIRouter, Depends, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import json
from bson import json_util

from app.db.mongodb.session import get_async_mongo_db as get_mongo_db

router = APIRouter()

@router.get(
    "/despesa/{nome}/{ano}/{mes}",
    summary="Busca despesas de um deputado por período",
    response_description="Despesas de um deputado para um ano e mês específicos."
)
async def read_despesas_deputado(
    nome: str,
    ano: int,
    mes: int,
    mongo_db = Depends(get_mongo_db)
):
    """
    **Busca as despesas mensais de um deputado federal.**
    
    - **nome**: Nome do deputado (ex: "Delegada Katarina").
    - **ano**: Ano da despesa (ex: 2025).
    - **mes**: Mês da despesa (ex: 2).
    
    A busca pelo nome não diferencia maiúsculas e minúsculas.
    """
    # Acessa a coleção "despesas-deputados"
    despesas_collection = mongo_db["despesas-deputados"]
    
    # Prepara a consulta para buscar por nome, ano e mês
    # Ajusta a string do nome para buscar por nomes parciais e sem acentos
    # A sua query original já usava um regex insensível a maiúsculas/minúsculas.
    # Agora vamos remover os acentos da string de entrada para uma busca mais robusta.
    import unicodedata
    nome_sem_acento = unicodedata.normalize('NFKD', nome).encode('ascii', 'ignore').decode('utf-8')
    
    query = {
        "deputado.nome": {"$regex": f"{nome_sem_acento}", "$options": "i"},
        "periodoDespesa.ano": ano,
        "periodoDespesa.mes": mes
    }
    
    # Executa a busca assíncrona
    despesa = await despesas_collection.find_one(query)
    
    if not despesa:
        raise HTTPException(status_code=404, detail=f"Despesa não encontrada para o deputado '{nome}' no período {mes}/{ano}.")
    
    # Serializa o documento para JSON, convertendo o ObjectId para string
    despesa_json = json.loads(json_util.dumps(despesa))
    
    return despesa_json
