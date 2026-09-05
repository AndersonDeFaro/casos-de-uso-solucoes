from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List, Optional

from app.models.users_api.user import User
from app.schemas.users_api.user import UserCreate, UserUpdate

# A biblioteca `passlib` é usada para hash de senhas
from passlib.context import CryptContext

# Cria um contexto para hash de senhas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.db = db

    async def get_user_by_email(self, email: str) -> Optional[User]:
        """
        Busca um usuário por email.
        """
        # A consulta é feita de forma assíncrona
        return self.db.query(User).filter(User.email == email).first()

    async def get_user(self, user_id: int) -> Optional[User]:
        """
        Busca um usuário por ID.
        """
        # A consulta é feita de forma assíncrona
        return self.db.query(User).filter(User.id == user_id).first()

    async def get_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        """
        Lista todos os usuários.
        """
        # A consulta é feita de forma assíncrona
        return self.db.query(User).offset(skip).limit(limit).all()

    async def create_user(self, user: UserCreate) -> User:
        """
        Cria um novo usuário.
        """
        # Hash da senha
        hashed_password = pwd_context.hash(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            password=hashed_password,
            is_active=True
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    async def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """
        Atualiza um usuário.
        """
        db_user = await self.get_user(user_id)
        if db_user:
            if user_update.username is not None:
                db_user.username = user_update.username
            if user_update.email is not None:
                db_user.email = user_update.email
            if user_update.is_active is not None:
                db_user.is_active = user_update.is_active
            self.db.commit()
            self.db.refresh(db_user)
        return db_user

    async def delete_user(self, user_id: int) -> None:
        """
        Deleta um usuário.
        """
        db_user = await self.get_user(user_id)
        if db_user:
            self.db.delete(db_user)
            self.db.commit()
