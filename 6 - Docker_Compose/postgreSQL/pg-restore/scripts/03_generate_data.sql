-- 03_generate_data.sql
\echo '=== Criando tabela e dados legítimos ==='

CREATE TABLE IF NOT EXISTS auditoria_transacoes (
    id SERIAL PRIMARY KEY,
    descricao TEXT,
    momento_registro TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

TRUNCATE auditoria_transacoes RESTART IDENTITY;

INSERT INTO auditoria_transacoes (descricao) VALUES
('Registro Legítimo 1'),
('Registro Legítimo 2'),
('Registro Legítimo 3');

SELECT id, descricao, momento_registro FROM auditoria_transacoes ORDER BY id;

\echo '=== Anote o timestamp abaixo (este será o target do PITR) ==='
SELECT NOW() AS timestamp_para_recovery;