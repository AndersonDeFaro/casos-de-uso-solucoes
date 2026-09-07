---- Criação da estrutura
CREATE TABLE contas_clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    saldo NUMERIC(15,2)
);

INSERT INTO contas_clientes (nome, saldo) VALUES
('Empresa A', 500000.00),
('Empresa B', 1200000.00);

---- Sessão 1 - Transação Esquecida
BEGIN;

UPDATE contas_clientes
SET saldo = saldo - 10000
WHERE id = 1;
-- NÃO EXECUTE COMMIT NEM ROLLBACK!

---- Sessão 2 - A vitima
SELECT * FROM contas_clientes
WHERE id = 1
FOR UPDATE;

----- Sessão 1 - DBA (Diagnostico)
SELECT
    pid,
    usename,
    state,
    wait_event_type,
    wait_event,
    query
FROM pg_stat_activity
WHERE query NOT LIKE '%pg_stat_activity%'
AND pid <> pg_backend_pid();

----- Quem bloqueia quem?
SELECT
blocked.pid AS pid_bloqueado,
blocking.pid AS pid_bloqueador,
71blocked.query AS query_bloqueada,
blocking.query AS query_bloqueadora,
blocked.wait_event_type,
blocked.wait_event
FROM pg_stat_activity AS blocked
JOIN pg_locks AS blocked_locks ON blocked.pid = blocked_locks.pid
JOIN pg_locks AS blocking_locks ON blocked_locks.locktype = blocking_locks.locktype
    AND blocked_locks.database IS NOT DISTINCT FROM blocking_locks.database
    AND blocked_locks.relation IS NOT DISTINCT FROM blocking_locks.relation
    AND blocked_locks.page IS NOT DISTINCT FROM blocking_locks.page
    AND blocked_locks.tuple IS NOT DISTINCT FROM blocking_locks.tuple
    AND blocked_locks.virtualxid IS NOT DISTINCT FROM blocking_locks.virtualxid
    AND blocked_locks.transactionid IS NOT DISTINCT FROM blocking_locks.transactionid
    AND blocked_locks.classid IS NOT DISTINCT FROM blocking_locks.classid
    AND blocked_locks.objid IS NOT DISTINCT FROM blocking_locks.objid
    AND blocked_locks.objsubid IS NOT DISTINCT FROM blocking_locks.objsubid
    AND blocked_locks.pid <> blocking_locks.pid
JOIN pg_stat_activity AS blocking ON blocking_locks.pid = blocking.pid
WHERE NOT blocked_locks.granted;

--- Versão Mais simples
SELECT
    a.pid,
    a.usename,
    a.state,
    a.query,
    l.locktype,
    l.mode,
    l.granted
FROM pg_stat_activity a
JOIN pg_locks l ON a.pid = l.pid
WHERE a.pid <> pg_backend_pid()
ORDER BY a.pid;

------- Tomada de Decisão
-- Opção 1: Cancelamento suave (tenta interromper a query atual)
SELECT pg_cancel_backend(PID_DO_VILAO);

-- Opção 2: Terminação forçada (expulsa a conexão)
SELECT pg_terminate_backend(PID_DO_VILAO);

------ Proteções Recomendadas
ALTER ROLE app_sistema SET lock_timeout = '5s';
ALTER ROLE app_sistema SET statement_timeout = '30s';