##### Migração direta entre servidores
pg_dump -h origem -U user1 -Fc db_prod | pg_restore -h destino -U user2 -d db_homolog --no-owner