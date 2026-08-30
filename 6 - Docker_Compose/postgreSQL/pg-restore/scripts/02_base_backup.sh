#!/bin/bash
set -e

BACKUP_DIR="./base_backup/base_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

echo "=== Realizando Base Backup ==="
echo "Destino: $BACKUP_DIR"

docker exec pg16-lab pg_basebackup \
  -U postgres \
  -D /tmp/basebackup \
  -Fp \
  -Xs \
  -P 

# Copiar o backup para o host
docker cp pg16-lab:/tmp/basebackup/. "$BACKUP_DIR/"

# Limpar dentro do container
docker exec pg16-lab rm -rf /tmp/basebackup

echo "Base backup concluído em: $BACKUP_DIR"