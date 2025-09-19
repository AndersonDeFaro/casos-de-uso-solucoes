from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional
import os


class Settings(BaseSettings):
    # Configurações da aplicação
    app_name: str = Field(default="Nome do Projeto", env="APP_NAME")
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    debug: bool = Field(default=False, env="DEBUG")
    secret_key: str = Field(env="SECRET_KEY")
    
    # PostgreSQL
    postgres_host: str = Field(env="POSTGRES_HOST")
    postgres_port: int = Field(default=5432, env="POSTGRES_PORT")
    postgres_db: str = Field(env="POSTGRES_DB")
    postgres_user: str = Field(env="POSTGRES_USER")
    postgres_password: str = Field(env="POSTGRES_PASSWORD")
    database_url: str = Field(env="DATABASE_URL")
    
    # MongoDB
    mongo_host: str = Field(env="MONGO_HOST")
    mongo_port: int = Field(default=27017, env="MONGO_PORT")
    mongo_db: str = Field(env="MONGO_DB")
    mongo_user: Optional[str] = Field(default=None, env="MONGO_USER")
    mongo_password: Optional[str] = Field(default=None, env="MONGO_PASSWORD")
    mongo_url: str = Field(env="MONGO_URL")
    
    # JWT
    jwt_secret_key: str = Field(env="JWT_SECRET_KEY")
    jwt_algorithm: str = Field(default="HS256", env="JWT_ALGORITHM")
    access_token_expire_minutes: int = Field(default=30, env="ACCESS_TOKEN_EXPIRE_MINUTES")
    
    # Ambiente
    environment: str = Field(default="development", env="ENVIRONMENT")
    
    class Config:
        env_file = ".env"
        case_sensitive = False

    @property
    def is_development(self) -> bool:
        return self.environment.lower() == "development"
    
    @property
    def is_production(self) -> bool:
        return self.environment.lower() == "production"


# Instância global das configurações
settings = Settings()