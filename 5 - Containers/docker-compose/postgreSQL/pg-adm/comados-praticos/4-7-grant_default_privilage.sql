-- Toda nova tabela criada no schema rh já nascerá com SELECT para o grupo de leitura
ALTER DEFAULT PRIVILEGES IN SCHEMA rh
GRANT SELECT ON TABLES TO grp_rh_read;
-- Toda nova tabela no schema rh já nascerá com permissões completas para os grupos de escrita e aplicação
ALTER DEFAULT PRIVILEGES IN SCHEMA rh
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO grp_rh_write, grp_app;