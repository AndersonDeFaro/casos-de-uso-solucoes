#### Restauração Custom / Directory
# 1. Criar o banco de destino (se ainda não existir)
docker exec -it pg16-lab psql -U postgres -c "DROP DATABASE IF EXISTS restore_lab;"
docker exec -it pg16-lab psql -U postgres -c "CREATE DATABASE restore_lab;"
# 2. Restaurar a partir do HOST
# OPs 1
docker exec -i pg16-lab pg_restore -U postgres -d restore_lab --no-owner < ./backups/postgres_completo.dump
# Restore a partir do CONTAINER
# OPs 2
docker cp ./backups/postgres_completo.dump pg16-lab:/tmp/
docker exec -i pg16-lab pg_restore -U postgres -d restore_lab --no-owner /tmp/postgres_completo.dump

#### Restore a partir de PLain Text
docker exec -i pg16-lab psql -U postgres -d restore_lab < ./backups/globals.sql

#### Restore Seletivo
docker exec -i pg16-lab pg_restore -U postgres -d restore_lab -t painel_sensores --no-owner < ./backups/postgres_completo.dump

#### Restauração Paralela
docker exec -i pg16-lab pg_restore -U postgres -d restore_lab -j 2 --no-owner /tmp/dump_paralelo

