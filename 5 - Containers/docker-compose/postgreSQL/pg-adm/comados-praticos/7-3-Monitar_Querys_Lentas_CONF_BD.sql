--- Adicionar Extension
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

--- Consulta Util
SELECT
    calls,
    ROUND(total_exec_time::numeric, 2) AS total_ms,
    ROUND(mean_exec_time::numeric, 2) AS media_ms,
    query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 10;