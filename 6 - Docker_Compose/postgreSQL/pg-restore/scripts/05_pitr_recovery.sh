#!/bin/bash
set -e

# ============================================
# CONFIGURAÇÃO - Altere o timestamp abaixo
# ============================================
RECOVERY_TARGET_TIME="2026-08-29 15:41:59.067003+00"   # <-- coloque o timestamp anotado
# ============================================

BACKUP_DIR=$(cat ./base_backup/latest_backup.txt 2>/dev/null || echo "")

if [ -z "$BACKUP_DIR" ] || [ ! -d "$BACKUP_DIR" ]; then
  echo "Erro: nenhum base backup encontrado. Execute 02_base_backup.sh primeiro."
  exit 1
fi

echo "=== Iniciando PITR ==="
echo "Target time : $RECOVERY_TARGET_TIME"
echo "Base backup : $BACKUP_DIR"

# 1. Parar o container
echo "Parando PostgreSQL..."
docker compose stop postgres

# 2. Limpar o data directory atual (cuidado!)
echo "Limpando data directory..."
rm -rf ./data/pgdata/*

# 3. Restaurar o base backup
echo "Restaurando base backup..."
cp -a "$BACKUP_DIR"/* ./data/pgdata/

# 4. Criar o arquivo de recovery (PostgreSQL 12+)
cat > ./data/recovery.signal <<EOF
# recovery.signal - força o PostgreSQL a entrar em recovery mode
EOF

# 5. Configurar o recovery target no postgresql.auto.conf (ou conf)
cat >> ./data/postgresql.auto.conf <<EOF

# === Configuração de PITR ===
restore_command = 'cp /var/lib/postgresql/wal_archive/%f %p'
recovery_target_time = '$RECOVERY_TARGET_TIME'
recovery_target_action = 'promote'
# recovery_target_inclusive = true   # true = inclui a transação do timestamp
EOF

echo "Arquivos de recovery configurados."

# 6. Subir o container novamente
echo "Subindo PostgreSQL em modo recovery..."
docker compose up -d

echo "Aguardando recovery..."
sleep 5

# Acompanhar os logs
docker logs -f pg16-lab --tail 50