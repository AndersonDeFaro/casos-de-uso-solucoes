from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from motor.motor_asyncio import AsyncIOMotorDatabase
from jose import JWTError, jwt
from typing import Optional

from app.core.config import settings
from app.db.session import get_db, get_mongo_db

# Security
security = HTTPBearer()

# Database Dependencies
def get_postgres_db() -> Session:
    """Dependency para obter sessão do PostgreSQL"""
    return Depends(get_db)

def get_mongodb() -> AsyncIOMotorDatabase:
    """Dependency para obter database do MongoDB"""
    return Depends(get_mongo_db)

# JWT Dependencies
def verify_token(token: str = Depends(security)) -> dict:
    """
    Verifica e decodifica o JWT token
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            token.credentials, 
            settings.jwt_secret_key, 
            algorithms=[settings.jwt_algorithm]
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception

def get_current_user(token_data: dict = Depends(verify_token)):
    """
    Obtém o usuário atual a partir do token
    """
    return token_data

# Optional Authentication (permite acesso sem token)
def get_current_user_optional(
    token: Optional[str] = Depends(security)
) -> Optional[dict]:
    """
    Obtém o usuário atual se o token for fornecido, senão retorna None
    """
    if not token:
        return None
    
    try:
        return verify_token(token)
    except HTTPException:
        return None

# Admin role dependency
def require_admin(current_user: dict = Depends(get_current_user)):
    """
    Requer que o usuário seja administrador
    """
    if not current_user.get("is_admin", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    return current_user

# Rate limiting (exemplo básico)
class RateLimiter:
    def __init__(self, times: int = 100, seconds: int = 60):
        self.times = times
        self.seconds = seconds
        self.requests = {}
    
    def __call__(self, request):
        # Implementação básica de rate limiting
        # Em produção, use Redis ou similar
        client_ip = request.client.host
        import time
        current_time = time.time()
        
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        
        # Remove requests antigas
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip] 
            if current_time - req_time < self.seconds
        ]
        
        # Verifica se excedeu o limite
        if len(self.requests[client_ip]) >= self.times:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded"
            )
        
        # Adiciona a request atual
        self.requests[client_ip].append(current_time)
        
        return True

# Instância do rate limiter
rate_limiter = RateLimiter(times=100, seconds=60)