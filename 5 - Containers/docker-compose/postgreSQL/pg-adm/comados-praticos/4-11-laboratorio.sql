--- PAsso 1
CREATE SCHEMA rh;
CREATE SCHEMA vendas;
CREATE SCHEMA financeiro;

--- Passo 2
-- Grupos de permissão
CREATE ROLE grp_rh_read WITH NOLOGIN;
CREATE ROLE grp_rh_write WITH NOLOGIN;
CREATE ROLE grp_vendas_read WITH NOLOGIN;
CREATE ROLE grp_vendas_write WITH NOLOGIN;
CREATE ROLE grp_financeiro WITH NOLOGIN;
CREATE ROLE grp_app WITH NOLOGIN; -- grupo da aplicação

--- Passo 3
CREATE ROLE ana_rh WITH LOGIN PASSWORD 'Senha@RH2026';
CREATE ROLE joao_vendas WITH LOGIN PASSWORD 'Senha@Vendas2026';
CREATE ROLE app_sistema WITH LOGIN PASSWORD 'Senha@App2026';
CREATE ROLE relatorios WITH LOGIN PASSWORD 'Senha@Rel2026';

--- Passo 4
GRANT grp_rh_read, grp_rh_write TO ana_rh;
GRANT grp_vendas_read, grp_vendas_write TO joao_vendas;
GRANT grp_app TO app_sistema;
GRANT grp_rh_read, grp_vendas_read TO relatorios; -- só leitura

--- Passo 5
-- USAGE nos schemas
GRANT USAGE ON SCHEMA rh TO grp_rh_read, grp_rh_write, grp_app;
GRANT USAGE ON SCHEMA vendas TO grp_vendas_read, grp_vendas_write, grp_app;
GRANT USAGE ON SCHEMA financeiro TO grp_financeiro, grp_app;
-- CREATE apenas para quem realmente precisa
GRANT CREATE ON SCHEMA rh TO grp_rh_write;
GRANT CREATE ON SCHEMA vendas TO grp_vendas_write;

--- Passo 6
CREATE TABLE rh.funcionarios (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL,
    cargo TEXT,
    salario NUMERIC(12,2)
);

CREATE TABLE vendas.pedidos (
    id SERIAL PRIMARY KEY,
    cliente TEXT,
    valor NUMERIC(12,2),
    data_pedido DATE DEFAULT CURRENT_DATE
)

--- Passo 7
-- RH
GRANT SELECT ON ALL TABLES IN SCHEMA rh TO grp_rh_read;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA rh TO grp_rh_write;
-- Vendas
GRANT SELECT ON ALL TABLES IN SCHEMA vendas TO grp_vendas_read;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA vendas TO
grp_vendas_write;
-- Aplicação (acesso completo aos dois módulos)
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA rh TO grp_app;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA vendas TO grp_app;
-- Liberação usuária Ana
GRANT grp_rh_read TO ana_rh;


--- Passo 8
ALTER DEFAULT PRIVILEGES IN SCHEMA rh
GRANT SELECT ON TABLES TO grp_rh_read;

ALTER DEFAULT PRIVILEGES IN SCHEMA rh
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO grp_rh_write, grp_app;

ALTER DEFAULT PRIVILEGES IN SCHEMA vendas
GRANT SELECT ON TABLES TO grp_vendas_read;

ALTER DEFAULT PRIVILEGES IN SCHEMA vendas
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO grp_vendas_write, grp_app;

--- Passo 9
-- Ver membership
SELECT r.rolname AS role,
        m.rolname AS member
FROM pg_auth_members am
JOIN pg_roles r ON r.oid = am.roleid
JOIN pg_roles m ON m.oid = am.member
ORDER BY 1, 2;

-- Testar como outro usuário
SET ROLE ana_rh;

SELECT current_user, session_user;

SELECT * FROM rh.funcionarios; -- deve funcionar

SELECT * FROM vendas.pedidos; -- deve falhar

RESET ROLE;

--- Passo 10
-- Quem tem permissão em uma tabela específica
SELECT grantee, privilege_type
FROM information_schema.role_table_grants
WHERE table_schema = 'rh' AND table_name = 'funcionarios';
-- Permissões de um usuário em todos os objetos
SELECT *
FROM information_schema.role_table_grants
WHERE grantee = 'ana_rh';