# Arquivo: app/db/postgres/session.py
from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# Importa as configurações globais da sua aplicação
from app.core.config import settings

# --- Conexão e Motor do PostgreSQL ---
# O 'pool_pre_ping' garante que a conexão está ativa antes de ser usada
engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Funções de Utilitário para o PostgreSQL ---

def get_db() -> Generator[Session, None, None]:
    """
    Cria uma sessão de banco de dados para o PostgreSQL e a fecha automaticamente.
    Esta é uma dependência injetável para rotas do FastAPI.
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def create_tables():
    """
    Cria todas as tabelas no banco de dados.
    Importe esta função no seu main.py ou em um script para inicializar o DB.
    """
    # A base precisa ser importada para que a metadados seja conhecida
    from app.db.postgres.base import Base
    Base.metadata.create_all(bind=engine)
