-- 04_simulate_error.sql
\echo '=== Simulando erro ==='

INSERT INTO auditoria_transacoes (descricao)
VALUES ('Registro indesejado pós-erro');

SELECT * FROM auditoria_transacoes ORDER BY id;

\echo '=== Executando DELETE (erro) ==='
DELETE FROM auditoria_transacoes;

SELECT COUNT(*) AS registros_apos_delete FROM auditoria_transacoes;