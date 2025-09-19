#!/bin/bash

# Este script inicializa o servidor Uvicorn com configurações otimizadas.

# Define o nome da sua aplicação no formato 'nome_do_arquivo:nome_do_objeto_FastAPI'
# Onde 'main' é o nome do arquivo e 'app' é a instância do FastAPI.
APP_NAME="app.main:app"

# Define o host para 0.0.0.0 para que a aplicação seja acessível de fora do container.
# Se for rodar localmente, pode ser 127.0.0.1.
HOST="0.0.0.0"

# Define a porta em que a aplicação irá rodar.
PORT="8000"

# Define o número de workers.
# Uma boa prática é usar (2 * número de núcleos da CPU) + 1.
WORKERS=${WORKERS:-$(($(nproc) * 2 + 1))}

# Define o loglevel para 'info' ou 'debug' para mais detalhes.
LOG_LEVEL="info"

# Executa o comando Uvicorn com as variáveis definidas acima.
exec uvicorn ${APP_NAME} \
  --host ${HOST} \
  --port ${PORT} \
  --workers ${WORKERS} \
  --log-level ${LOG_LEVEL}