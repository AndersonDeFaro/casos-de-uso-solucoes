### Configuração config/postgresql.conf
wal_level = replica
archive_mode = on
archive_command = 'test ! -f /caminho/arquivo/%f && cp %p /caminho/arquivo/%f'

