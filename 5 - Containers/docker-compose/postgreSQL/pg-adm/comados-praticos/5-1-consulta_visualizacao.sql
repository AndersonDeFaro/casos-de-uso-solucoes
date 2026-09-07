-- Consulta prática de visualização
SELECT
    n.nspname AS schema,
    c.relname AS objeto,
    CASE c.relkind
        WHEN 'r' THEN 'Tabela'
        WHEN 'i' THEN 'Índice'
        WHEN 'S' THEN 'Sequência'
        WHEN 'v' THEN 'View'
        WHEN 'm' THEN 'Materialized View'
        WHEN 'p' THEN 'Tabela Particionada'
        WHEN 't' THEN 'Tabela TOAST'
        WHEN 'f' THEN 'Foreign Table'
        ELSE c.relkind::text
    END AS tipo,
    c.oid,
    c.relfilenode
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname NOT IN ('pg_catalog', 'information_schema')
ORDER BY 1, 3, 2;