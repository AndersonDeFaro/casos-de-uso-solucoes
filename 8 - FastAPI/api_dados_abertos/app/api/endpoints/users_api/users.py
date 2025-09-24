from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.dependencies import get_current_user
# A importação do SQLAlchemy (PostgreSQL) agora vem de seu próprio módulo
from app.db.postgres.session import get_db
from app.schemas.users_api.user import UserCreate, UserResponse, UserUpdate
from app.services.users_api.user_service import UserService

router = APIRouter()

@router.get("/", response_model=List[UserResponse])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Listar usuários (PostgreSQL)
    """
    user_service = UserService(db)
    users = await user_service.get_users(skip=skip, limit=limit)
    return users

@router.post("/", response_model=UserResponse)
async def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Criar novo usuário
    """
    user_service = UserService(db)
    
    # Verificar se usuário já existe
    existing_user = await user_service.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    created_user = await user_service.create_user(user)
    return created_user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Obter usuário por ID
    """
    user_service = UserService(db)
    user = await user_service.get_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int,
    user_update: UserUpdate,
    db: Session = Depends(get_db)
):
    """
    Atualizar usuário
    """
    user_service = UserService(db)
    
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = await user_service.update_user(user_id, user_update)
    return updated_user

@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """
    Deletar usuário
    """
    user_service = UserService(db)
    
    user = await user_service.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await user_service.delete_user(user_id)
    return {"message": "User deleted successfully"}
