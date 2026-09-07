-- Criar usuário de monitoramento
CREATE ROLE usuario_monitoramento WITH LOGIN PASSWORD 'SenhaForte@2026';
-- Conceder permissão da role pg_monitor
GRANT pg_monitor TO usuario_monitoramento;