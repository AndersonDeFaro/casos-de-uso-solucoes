# Use uma imagem Python leve e otimizada para ser a base.
# A imagem python:3.11-slim-bookworm é uma ótima escolha.
FROM python:3.11-slim-bookworm

# Define a variável de ambiente para que o Python não crie arquivos .pyc.
ENV PYTHONDONTWRITEBYTECODE 1

# Define a variável de ambiente para que a saída do Python seja enviada diretamente para o terminal.
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho no contêiner.
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner.
# A ordem é importante para o cache do Docker. Copiar o requirements.txt primeiro
# permite que esta camada seja recarregada apenas se o arquivo mudar.
COPY ./requirements.txt /app/requirements.txt

# Instala as dependências.
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copia todo o restante do código da sua aplicação para o contêiner.
COPY . /app

# Torna o script uvicorn.sh executável.
RUN chmod +x /app/uvicorn.sh

# Comando de inicialização.
# O Dockerfile usa o CMD para definir o comando padrão.
# O docker-compose pode sobrescrever esse comando com o `command: ./uvicorn.sh`.
CMD ["/app/uvicorn.sh"]