SELECT relname,
    oid,
    relfilenode,
    relkind
FROM pg_class
WHERE relname = 'funcionarios';