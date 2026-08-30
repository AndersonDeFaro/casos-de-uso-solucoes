# 1. Preparar e subir
chmod +x scripts/*.sh
./scripts/01_prepare.sh

# 2. Fazer base backup (com o banco vazio ou quase vazio)
./scripts/02_base_backup.sh

# 3. Gerar dados legítimos e anotar o timestamp
docker exec -i pg16-lab psql -U postgres < scripts/03_generate_data.sql
# → Anote o valor de "timestamp_para_recovery"

# 4. Simular o erro
docker exec -i pg16-lab psql -U postgres < scripts/04_simulate_error.sql

# 5. Editar o timestamp no script 05 e executar o recovery
#    (abra o arquivo e coloque o timestamp anotado)
./scripts/05_pitr_recovery.sh

# 6. Validar
docker exec -i pg16-lab psql -U postgres < scripts/06_validate.sql