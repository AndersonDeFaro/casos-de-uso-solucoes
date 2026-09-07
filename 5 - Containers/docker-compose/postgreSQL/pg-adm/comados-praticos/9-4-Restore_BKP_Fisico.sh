#### Limpar diretório de dados
rm -rf data/pgdata/*

#### Copiar BASE Backup
cp -rf base_backup/* data/pgdata/

#### Apagar archive velhos de WAL
rm -rf data/pgdata/pg_wal/*

#### Criação de arquivo recovery.sinal
# Criação do Arquivo Recovery
touch data/pgdata/recovery.signal
chown 999:999 data/pgdata/recovery.signal

#### Config postgresql.auto.conf
restore_command = 'cp /var/lib/postgresql/wal_archive/%f %p'
recovery_target_time = '2026-08-25 12:30:45.123456-03' -- timestamp anotado
recovery_target_inclusive = true

#### Subir container do PostgreSQL
docker compose up -d

#### Após verificar se o Banco de Dados está restaurado no ponto esperado
# Conectar e promover
docker exec -it pg16-lab psql -U postgres -c "SELECT pg_promote();"

# Verificar se saiu do recovery
docker exec -it pg16-lab psql -U postgres -c "SELECT pg_is_in_recovery();"
# Deve retornar: f
