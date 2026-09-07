-- Role de usuário (pode fazer login)
CREATE ROLE usuario_app WITH LOGIN PASSWORD 'SenhaForte@2026';
-- Role de grupo (não pode fazer login)
CREATE ROLE app_read WITH NOLOGIN;
-- Alias (CREATE USER = CREATE ROLE ... WITH LOGIN)
CREATE USER analista WITH PASSWORD 'SenhaForte@2026';