##### Verificar SO
# Entrar no container
docker exec -it pg16-lab bash
# Ir para o $PGDATA
cd /var/lib/postgresql/data/pgdata
# Listar pastas dos bancos
ls -l base/
# Entrar na pasta de um banco específico (use o OID descoberto)
ls -l base/5/