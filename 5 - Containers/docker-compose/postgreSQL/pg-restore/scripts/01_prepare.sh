#!/bin/bash
set -e

echo "=== Preparando ambiente PITR ==="

# Criar pastas necessárias
mkdir -p backups wal_archive data config scripts

# Garantir permissões (importante dentro do container)
chmod 700 data wal_archive backups 2>/dev/null || true

echo "Pastas criadas."
echo "Subindo o container..."
docker compose up -d

echo "Aguardando PostgreSQL ficar pronto..."
until docker exec pg16-lab pg_isready -U postgres > /dev/null 2>&1; do
  sleep 1
done

echo "PostgreSQL pronto."