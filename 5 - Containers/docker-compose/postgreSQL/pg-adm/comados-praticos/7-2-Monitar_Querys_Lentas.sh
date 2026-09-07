#Edit config/postgresql.conf
shared_preload_libraries = 'pg_stat_statements'

## Reset container
docker compose restart