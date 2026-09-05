# Arquivo: app/db/postgres/base.py
from sqlalchemy.ext.declarative import declarative_base

# A base declarativa é onde todos os modelos do SQLAlchemy para o PostgreSQL herdam
Base = declarative_base()