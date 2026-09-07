#### Preapração Diretório de Backup - HOST
# Criar diretórios
mkdir -p ./wal_archive
mkdir -p ./base_backup
# Conceder permissão ao Postgres
chown -Rf 999:999 wal_archive/ base_backup/

#### Ajustar postgresql.conf
wal_level = replica
archive_mode = on
archive_command = 'test ! -f /var/lib/postgresql/wal_archive/%f && cp %p
/var/lib/postgresql/wal_archive/%f'

#### Ajustar cocker-compose.yml
volumes:
- ./data:/var/lib/postgresql/data
- ./config:/etc/postgresql
- ./wal_archive:/var/lib/postgresql/wal_archive

#### Reiniciar ambiente
docker compose down
docker compose up -d

#### Validar configuração
docker exec -it pg16-lab psql -U postgres -c "SHOW archive_mode;"
docker exec -it pg16-lab psql -U postgres -c "SHOW archive_command;"

#### Forçar Rotação de WAL
docker exec -it pg16-lab psql -U postgres -c "SELECT pg_switch_wal();"

#### Verificar se arquivo apareceu no diretório de archive WAL
ls -lh ./wal_archive/

##### Adicionar configuração de replica no pg_hba.conf
# Linha permitindo conexões do tipo replication
local       replication         postgres            trust

#### Executar backup físico
docker exec -it pg16-lab pg_basebackup \
-U postgres \
-D /tmp/base_backup \
-Fp \
-X stream \
-P

#### Copiar resultado do backup físico para o host
# Rotacionar WAL
docker exec -it pg16-lab psql -U postgres -c "SELECT pg_switch_wal();"
docker exec -it pg16-lab psql -U postgres -c "SELECT pg_switch_wal();"
# Copiar Backup
sudo docker cp pg16-lab:/tmp/base_backup .
