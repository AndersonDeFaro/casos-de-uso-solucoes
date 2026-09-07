-- Tamanho do banco inteiro
SELECT pg_size_pretty(pg_database_size(current_database()));

-- Tamanho detalhado por tabela
SELECT
    relname AS objeto,
    pg_size_pretty(pg_table_size(oid)) AS dados,
    pg_size_pretty(pg_indexes_size(oid)) AS indices,
    pg_size_pretty(pg_total_relation_size(oid)) AS total
FROM pg_class
WHERE relkind = 'r'
  AND relnamespace = 'rh'::regnamespace
ORDER BY pg_total_relation_size(oid) DESC;