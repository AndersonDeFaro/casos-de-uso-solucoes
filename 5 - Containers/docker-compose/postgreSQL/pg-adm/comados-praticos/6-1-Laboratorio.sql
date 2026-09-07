--- Passo 1
CREATE TABLE painel_sensores (
    id SERIAL PRIMARY KEY,
    codigo_sensor VARCHAR(20),
    status_atual VARCHAR(20),
    ultima_leitura NUMERIC(5,2)
);

--- Passo 2
INSERT INTO painel_sensores (codigo_sensor, status_atual, ultima_leitura)
SELECT
'SNS-' || i,
'OPERACIONAL',
(random() * 100)::NUMERIC(5,2)
FROM generate_series(1, 10000) AS i;

--- Passo 3
SELECT xmin, xmax, id, codigo_sensor, status_atual
FROM painel_sensores
LIMIT 5;

--- Passo 4
SELECT
    relname AS tabela,
    n_live_tup AS tuplas_vivas,
    n_dead_tup AS tuplas_mortas
FROM pg_stat_user_tables
WHERE relname = 'painel_sensores';

--- Passo 5
SELECT pg_size_pretty(pg_relation_size('painel_sensores')) AS tamanho_tabela;

--- Passo 6
ALTER TABLE painel_sensores SET (autovacuum_enabled = false);

--- Passo 7
UPDATE painel_sensores SET status_atual = 'ALERTA', ultima_leitura = 99.9;
UPDATE painel_sensores SET status_atual = 'CRITICO', ultima_leitura = 12.4;
UPDATE painel_sensores SET status_atual = 'ESTAVEL', ultima_leitura = 45.2;

--- Passo 8
SELECT
    relname,
    n_live_tup,
    n_dead_tup
FROM pg_stat_user_tables
WHERE relname = 'painel_sensores';

--- Passo 9
SELECT pg_size_pretty(pg_relation_size('painel_sensores')) AS tamanho_tabela;

--- Passo 10
-- Limpeza normal (libera espaço internamente)
VACUUM VERBOSE painel_sensores;
-- Atualiza estatísticas
ANALYZE painel_sensores;
-- (Opcional e perigoso em produção) Devolve espaço ao SO
VACUUM FULL VERBOSE painel_sensores;

--- Passo 11
ALTER TABLE painel_sensores SET (autovacuum_enabled = true);

