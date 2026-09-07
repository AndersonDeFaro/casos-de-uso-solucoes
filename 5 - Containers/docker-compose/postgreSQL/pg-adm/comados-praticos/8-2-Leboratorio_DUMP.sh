###### Criar diretório de Backup
mkdir -p ./backups

###### Gerar GP DUMP
### OPs 1 - Dentro do host (recomendado)
# Forma correta (sem -t)
docker exec -i pg16-lab pg_dump -U postgres -Fc -d postgres > ./backups/postgres_completo.dump

### OPs 2 - Dentro do container (não recomendado)
docker exec -it pg16-lab bash
pg_dump -U postgres -Fc -d postgres -f /tmp/postgres_completo.dump

# Copiar para o host
docker cp pg16-lab:/tmp/postgres_completo.dump ./backups/

###### DUMP apena dos SCHEMAS
docker exec -i pg16-lab pg_dump -U postgres -Fc -n rh -d postgres > ./backups/schema_rh.dump

###### DUMP apenas da estrutura do banco de dados (sem dados)
docker exec -i pg16-lab pg_dump -U postgres -Fc -s -d postgres > ./backups/somente_estrutura.dump

##### DUMP apena dos dados
docker exec -i pg16-lab pg_dump -U postgres -Fc -a -d postgres > ./backups/somente_dados.dump

##### DUMP Paralelo (Forma Directory)
# Gerar o DUMP (Paralelo)
docker exec -i pg16-lab pg_dump -U postgres -Fd -j 2 -d postgres -f /tmp/dump_paralelo
# Copiar o DUMP para o HOST
docker cp pg16-lab:/tmp/dump_paralelo ./backups/

##### Capturar Objetos globais
docker exec -i pg16-lab pg_dumpall -U postgres --globals-only > ./backups/globals.sql