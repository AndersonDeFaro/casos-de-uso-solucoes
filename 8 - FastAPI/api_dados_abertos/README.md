# Projeto FastAPI - nome_projeto

Este diretório contém a implementação de uma API utilizando o framework [FastAPI](https://fastapi.tiangolo.com/), seguindo uma arquitetura organizada para facilitar a manutenção, escalabilidade e testes.

## Estrutura de Diretórios

```
8 - FastAPI/
/nome_do_projeto
├── /app
	├── /api
	│   ├── /endpoints
	│   │   ├── /system_a
	│   │   │   ├── __init__.py
	│   │   │   ├── users.py
	│   │   │   └── products.py
	│   │   ├── /system_b
	│   │   │   ├── __init__.py
	│   │   │   ├── clients.py
	│   │   │   └── orders.py
	│   │   ├── __init__.py
	│   │   └── router.py
│   ├── /core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── dependencies.py
│   ├── /db
│   │   ├── __init__.py
│   │   ├── base.py
│   │   └── session.py
│   ├── /models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── /schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── item.py
│   ├── /services
│   │   ├── __init__.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   ├── /repositories
│   │   ├── __init__.py
│   │   ├── user_repository.py
│   │   └── item_repository.py
│   └── main.py
├── /tests
│   ├── __init__.py
│   ├── test_main.py
│   └── /api
│       └── test_endpoints.py
├── .env
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── README.md
├── requirements.txt
└── uvicorn.sh
```

### Descrição dos Diretórios

- **app/main.py**  
  Ponto de entrada da aplicação FastAPI.

- **app/api/v1/endpoints/**  
  Define os endpoints da API, organizados por recurso.

- **app/core/**  
  Configurações centrais da aplicação (ex: variáveis de ambiente).

- **app/models/**  
  Modelos ORM (ex: SQLAlchemy) que representam as tabelas do banco de dados.

- **app/schemas/**  
  Schemas Pydantic para validação e serialização de dados.

- **app/db/**  
  Configuração da sessão e conexão com o banco de dados.

- **tests/**  
  Testes automatizados para os endpoints e funcionalidades.

- **requirements.txt**  
  Lista de dependências do projeto.

---

## Exemplo de Código na Arquitetura

### 1. Modelo (app/models/item.py)
```python
from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
```

### 2. Schema (app/schemas/item.py)
```python
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
```

### 3. CRUD (app/crud/item.py)
```python
from sqlalchemy.orm import Session
from app.models.item import Item
from app.schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Item).offset(skip).limit(limit).all()
```

### 4. Endpoint (app/api/v1/endpoints/items.py)
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.item import Item, ItemCreate
from app.crud.item import create_item, get_items
from app.db.session import get_db

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_new_item(item: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, item)

@router.get("/items/", response_model=list[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items(db, skip=skip, limit=limit)
```

### 5. main.py (app/main.py)
```python
from fastapi import FastAPI
from app.api.v1.endpoints import items

app = FastAPI()

app.include_router(items.router, prefix="/api/v1")
```

---

## Como Executar

1. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
2. Execute a aplicação:
   ```
   uvicorn app.main:app --reload
   ```
3. Acesse a documentação interativa em:  
   [http://localhost:8000/docs](http://localhost:8000/docs)

---

Sinta-se à vontade para adaptar a estrutura conforme as