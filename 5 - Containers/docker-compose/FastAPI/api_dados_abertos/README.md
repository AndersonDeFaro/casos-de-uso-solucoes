# API Dados Abertos

API desenvolvida com FastAPI para disponibilizar recursos de dados abertos. A aplicação inicializa estruturas no PostgreSQL, mantém conexão assíncrona com MongoDB e expõe rotas versionadas sob `/api/v1`.

## Serviços

O `docker-compose.yml` inicia os seguintes serviços:

- `api`: aplicação FastAPI exposta na porta `8000`.
- `postgres`: banco relacional usado pela aplicação.
- `mongodb`: banco de documentos usado pela aplicação.

## Estrutura

- `app/main.py`: cria a aplicação, configura CORS, ciclo de vida e rotas base.
- `app/api/endpoints/`: routers organizados por recurso, incluindo deputados federais e usuários.
- `app/core/`: configurações e dependências compartilhadas.
- `app/db/`: sessões e conexões com PostgreSQL e MongoDB.
- `app/models/`, `app/schemas/`, `app/repositories/` e `app/services/`: camadas de domínio e acesso a dados.
- `Dockerfile` e `uvicorn.sh`: imagem e comando de inicialização do serviço da API.

## Como executar com Docker

1. Copie ou ajuste o arquivo `.env` com variáveis adequadas ao seu ambiente. Não publique credenciais reais.
2. Na pasta deste projeto, execute:

   ```bash
   docker compose up --build
   ```

3. Acesse os endpoints:

   - Documentação interativa: `http://localhost:8000/docs`
   - Verificação de saúde: `http://localhost:8000/health`
   - Rota raiz: `http://localhost:8000/`

4. Para encerrar os serviços, execute:

   ```bash
   docker compose down
   ```

## Desenvolvimento local

Instale as dependências e execute o servidor apenas quando PostgreSQL e MongoDB estiverem acessíveis com as variáveis configuradas:

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Observações

As tabelas do PostgreSQL são verificadas na inicialização e a conexão assíncrona com MongoDB é aberta durante o ciclo de vida da API. Antes de executar cargas ou alterações de dados, valide a configuração em um ambiente isolado.