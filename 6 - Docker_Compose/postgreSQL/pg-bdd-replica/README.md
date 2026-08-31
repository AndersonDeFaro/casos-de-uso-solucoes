
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

## Parametros Importante no Docker

### Ajustar nome da replicar pra configurar sicronização
```
# Garante application_name correto
echo "primary_conninfo = 'host=pg-primary port=5432 user=replicador password=SenhaMestre123# application_name=pg-replica1'" \
> /var/lib/postgresql/data/postgresql.auto.conf
echo "primary_slot_name = 'replica1_slot'" \
>> /var/lib/postgresql/data/postgresql.auto.conf
```            

## Scripts pra verificar se a replica está funcionando

### 1. Verificar se a Réplica está Conectada (Rode no Primary)
```
SELECT 
    application_name AS nome_da_replica,
    client_addr AS ip_da_replica,
    backend_start AS conectada_em,
    state AS status_do_streaming,
    sync_state AS tipo_de_sincronizacao
FROM pg_stat_replication;
```

### 2. Verificar o Atraso (Lag) da Replicação (Rode no Primary)
```
SELECT
    application_name AS nome_da_replica,
    client_addr AS ip_da_replica,
    pg_wal_lsn_diff(pg_current_wal_lsn(), sent_lsn) AS lag_envio_bytes,
    pg_wal_lsn_diff(sent_lsn, write_lsn) AS lag_escrita_bytes,
    pg_wal_lsn_diff(write_lsn, flush_lsn) AS lag_disco_bytes,
    pg_wal_lsn_diff(flush_lsn, replay_lsn) AS lag_aplicacao_bytes
FROM pg_stat_replication;
```

### 3. Confirmar se a Instância Atual é Primary ou Réplica
```
SELECT 
    pg_is_in_recovery() AS eh_replica,
    CASE 
        WHEN pg_is_in_recovery() = true THEN 'RÉPLICA (Apenas Leitura)'
        ELSE 'PRIMARY (Leitura e Escrita)'
    END AS modo_do_servidor;
```