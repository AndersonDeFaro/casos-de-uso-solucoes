from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# Classe base para os dados de usuário
class UserBase(BaseModel):
    username: str = Field(..., example="john.doe")
    email: EmailStr = Field(..., example="john.doe@example.com")

# Classe para a criação de um novo usuário
class UserCreate(UserBase):
    password: str = Field(..., example="SenhaForte123")

# Classe para a resposta de um usuário (oculta a senha)
class UserResponse(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True

# Classe para a atualização de um usuário (campos opcionais)
class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
