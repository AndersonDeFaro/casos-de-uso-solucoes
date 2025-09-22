from typing import Optional
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User # Assumindo que você tem um modelo SQLAlchemy para o usuário

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> Optional[UserResponse]:
        """
        Busca um usuário pelo email.
        """
        user = self.db.query(User).filter(User.email == email).first()
        if user:
            return UserResponse.model_validate(user)
        return None

    def create_user(self, user_in: UserCreate) -> UserResponse:
        """
        Cria um novo usuário no banco de dados.
        """
        # Aqui, você pode adicionar a lógica para hashear a senha antes de salvar
        # from app.core.security import get_password_hash
        # hashed_password = get_password_hash(user_in.password)
        
        db_user = User(
            username=user_in.username,
            email=user_in.email,
            password=user_in.password, # Mude para 'hashed_password' quando a segurança for implementada
            is_active=True
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserResponse.model_validate(db_user)

    def get_users(self, skip: int = 0, limit: int = 100) -> list[UserResponse]:
        """
        Retorna uma lista de usuários paginada.
        """
        users = self.db.query(User).offset(skip).limit(limit).all()
        return [UserResponse.model_validate(user) for user in users]
