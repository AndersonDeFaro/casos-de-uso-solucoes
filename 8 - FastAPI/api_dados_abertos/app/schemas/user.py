from pydantic import BaseModel, Field
from typing import Optional

# Classe base para os dados de usuário
class UserBase(BaseModel):
    username: str = Field(..., example="john.doe")
    email: str = Field(..., example="john.doe@example.com")

# Classe para criação de um novo usuário (inclui a senha)
class UserCreate(UserBase):
    password: str = Field(..., example="SenhaForte123")

# Classe para a resposta de um usuário (oculta a senha)
class UserResponse(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True

# Classe para atualizar um usuário (campos opcionais)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
