from fastapi import APIRouter
from . import users

router = APIRouter(prefix="/users_api", tags=["Controle de Usuários"])

router.include_router(users.router)