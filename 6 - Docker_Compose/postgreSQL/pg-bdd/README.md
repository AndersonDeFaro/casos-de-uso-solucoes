
## pg_basebackup

### Flags do `pg_basebackup`:
 - `-R`: Cria automaticamente standby.signal + escreve primary_conninfo no postgresql.auto.conf
 - `-Xs` / `-X stream`: Faz streaming do WAL durante o backup (evita perder WAL)
 - `-Fp`: Formato plain (diretório normal)
 - `-P`: Mostra progresso
 - `-S slot`: Usa um replication slot (recomendado)


## Comandos Docker

### Subir tudo
docker compose up -d

### Ver logs da réplica
docker logs -f pg-replica1

### No primary: ver se a réplica está conectada
docker exec -it pg-bdd-primary psql -U postgres -c "SELECT * FROM pg_stat_replication;"

### Teste de leitura na réplica
docker exec -it pg-replica1 psql -U postgres -d 

bdd_pos -c "SELECT pg_is_in_recovery();"
##### deve retornar 't' (true)