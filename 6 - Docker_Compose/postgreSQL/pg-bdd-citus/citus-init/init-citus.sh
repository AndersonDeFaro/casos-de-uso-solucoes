#!/bin/bash
set -euo pipefail

export PATH="/usr/lib/postgresql/16/bin:$PATH"

COORD="citus-coordenator"
WORK1="citus-work1"
WORK2="citus-work2"
DB="citus"
USER="postgres"
PORT="5432"

echo ">>> Aguardando nodes ficarem prontos..."

wait_pg() {
  local host="$1"
  until pg_isready -h "$host" -p "$PORT" -U "$USER" >/dev/null 2>&1; do
    echo "    aguardando $host..."
    sleep 2
  done
  echo "    $host OK"
}

wait_pg "$COORD"
wait_pg "$WORK1"
wait_pg "$WORK2"

psql_c() {
  local host="$1"
  shift
  PGPASSWORD="${POSTGRES_PASSWORD:-postgres}" \
    psql -h "$host" -p "$PORT" -U "$USER" -d "$DB" -v ON_ERROR_STOP=1 "$@"
}

echo ">>> Criando extensão citus em todos os nodes..."
psql_c "$COORD" -c "CREATE EXTENSION IF NOT EXISTS citus;"
psql_c "$WORK1" -c "CREATE EXTENSION IF NOT EXISTS citus;"
psql_c "$WORK2" -c "CREATE EXTENSION IF NOT EXISTS citus;"

echo ">>> Configurando coordenador e registrando workers..."
psql_c "$COORD" -c "SELECT citus_set_coordinator_host('${COORD}', ${PORT});"

# Evita erro se o node já estiver registrado
psql_c "$COORD" -c "
DO \$\$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_dist_node WHERE nodename = '${WORK1}' AND nodeport = ${PORT}
  ) THEN
    PERFORM citus_add_node('${WORK1}', ${PORT});
  END IF;
END
\$\$;
"

psql_c "$COORD" -c "
DO \$\$
BEGIN
  IF NOT EXISTS (
    SELECT 1 FROM pg_dist_node WHERE nodename = '${WORK2}' AND nodeport = ${PORT}
  ) THEN
    PERFORM citus_add_node('${WORK2}', ${PORT});
  END IF;
END
\$\$;
"

echo ">>> Verificação final..."
psql_c "$COORD" -c "SELECT * FROM citus_get_active_worker_nodes() ORDER BY node_name;"

COUNT=$(psql_c "$COORD" -Atc "SELECT count(*) FROM citus_get_active_worker_nodes();")
if [ "$COUNT" -ge 2 ]; then
  echo ">>> Cluster Citus OK: ${COUNT} worker(s) ativo(s)."
  exit 0
else
  echo ">>> ERRO: esperava 2 workers, encontrou ${COUNT}."
  exit 1
fi