-- Ou via SQL
SELECT * FROM pg_default_acl;

-- Remover uma regra
ALTER DEFAULT PRIVILEGES IN SCHEMA rh
REVOKE SELECT ON TABLES FROM grp_rh_read;