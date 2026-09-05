-- 06_validate.sql
\echo '=== Validação após PITR ==='

SELECT COUNT(*) AS total_registros FROM auditoria_transacoes;

SELECT id, descricao, momento_registro
FROM auditoria_transacoes
ORDER BY id;

\echo '=== Se o recovery funcionou, você deve ver apenas os registros legítimos ==='