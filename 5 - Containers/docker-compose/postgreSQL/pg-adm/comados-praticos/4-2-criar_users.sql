-- Criando a role João
CREATE ROLE joao WITH LOGIN PASSWORD 'SenhaForte@2026'
-- Adicionar usuário ao grupo
GRANT app_read TO joao;
-- Remover usuário do grupo
REVOKE app_read FROM joao;