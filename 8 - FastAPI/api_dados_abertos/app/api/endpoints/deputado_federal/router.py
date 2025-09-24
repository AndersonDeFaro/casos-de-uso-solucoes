from fastapi import APIRouter

from . import estado
from . import despesa

router = APIRouter(prefix="/deputado_federal", tags=["Deputados Federais"])

router.include_router(estado.router)
router.include_router(despesa.router)