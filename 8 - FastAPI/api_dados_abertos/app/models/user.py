from sqlalchemy import Column, Integer, String, Boolean
from app.db.base import Base

class User(Base):
    """
    Modelo SQLAlchemy para a tabela 'users' no banco de dados.
    """
    __tablename__ = "users"
    __table_args__ = {'schema': 'api'}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
