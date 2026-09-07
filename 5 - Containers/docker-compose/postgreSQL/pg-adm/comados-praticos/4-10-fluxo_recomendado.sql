-- 1. Corrige o presente (tabelas que já existem)
GRANT SELECT ON ALL TABLES IN SCHEMA rh TO grp_rh_read;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA rh TO grp_rh_write,
grp_app;

-- 2. Garante o futuro (tabelas que ainda serão criadas)
ALTER DEFAULT PRIVILEGES IN SCHEMA rh
GRANT SELECT ON TABLES TO grp_rh_read;

ALTER DEFAULT PRIVILEGES IN SCHEMA rh
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO grp_rh_write, grp_app;