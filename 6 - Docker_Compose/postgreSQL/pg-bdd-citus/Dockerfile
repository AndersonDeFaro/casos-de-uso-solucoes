FROM postgres:16

# Instala as ferramentas necessárias para compilar a extensão em C
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    autoconf \
    flex \
    libcurl4-openssl-dev \
    postgresql-server-dev-16 \
    liblz4-dev \
    libzstd-dev \
    libssl-dev \
    libreadline-dev \
    libicu-dev \
    libkrb5-dev \
    libpam0g-dev \
    libselinux1-dev \
    libxslt1-dev \
    uuid-dev \
    && rm -rf /var/lib/apt/lists/*

# Clona o código-fonte do Citus e compila nativamente para ARM64 definindo o PATH do Postgres
RUN git clone --depth 1 --branch v12.1.0 https://github.com/citusdata/citus.git /usr/src/citus \
    && cd /usr/src/citus \
    && export PATH="/usr/lib/postgresql/16/bin:$PATH" \
    && ./configure \
    && make \
    && make install \
    && rm -rf /usr/src/citus

# Configura o Postgres para carregar o Citus mapeado na inicialização
RUN echo "shared_preload_libraries = 'citus'" >> /usr/share/postgresql/postgresql.conf.sample

# Garante autenticação livre na rede interna do Docker para comunicação dos nós
ENV POSTGRES_HOST_AUTH_METHOD=trust