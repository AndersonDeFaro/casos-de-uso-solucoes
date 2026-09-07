SELECT oid, datname
FROM pg_database
WHERE datname = current_database();