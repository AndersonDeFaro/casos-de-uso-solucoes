-- Cria o usuário de replicação (só executa na primeira inicialização)
CREATE USER replicador WITH REPLICATION ENCRYPTED PASSWORD 'SenhaMestre123#';

-- Cria o slot físico (recomendado)
SELECT pg_create_physical_replication_slot('replica1_slot');