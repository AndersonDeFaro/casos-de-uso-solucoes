from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorDatabase
from typing import List

from app.core.dependencies import get_current_user
from app.db.session import get_db, get_mongo_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Listar usuários (PostgreSQL + MongoDB)
    """
    user_service = UserService(db, mongo_db)
    users = await user_service.get_users(skip=skip, limit=limit)
    return users

@router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db)
):
    """
    Criar novo usuário
    """
    user_service = UserService(db, mongo_db)
    
    # Verificar se usuário já existe
    existing_user = await user_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    created_user = await user_service.create_user(user)
    return created_user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Obter usuário por ID
    """
    user_service = UserService(db, mongo_db)
    user = await user_service.get_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserCreate,
    db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Atualizar usuário
    """
    user_service = UserService(db, mongo_db)
    
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = await user_service.update_user(user_id, user_update)
    return updated_user

@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    mongo_db: AsyncIOMotorDatabase = Depends(get_mongo_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Deletar usuário
    """
    user_service = UserService(db, mongo_db)
    
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}