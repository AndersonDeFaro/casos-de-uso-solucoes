from fastapi import APIRouter
from . import users
from . import products

router = APIRouter(prefix="/system_a", tags=["system_a"])

router.include_router(users.router)
router.include_router(products.router)