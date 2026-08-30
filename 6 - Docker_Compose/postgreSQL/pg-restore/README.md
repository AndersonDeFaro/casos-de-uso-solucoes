# PostgreSQL PITR (Point-in-Time Recovery) Lab

Laboratório para simular e validar recuperação de desastres no PostgreSQL usando **base backup + WAL archiving + PITR**.


## Estrutura do projeto

```
pg-restore/
├── docker-compose.yml
├── config/
│   ├── postgresql.conf
│   └── pg_hba.conf
├── scripts/
│   ├── 01_prepare.sh
│   ├── 02_base_backup.sh
│   ├── 03_generate_data.sql
│   ├── 04_simulate_error.sql
│   ├── 05_pitr_recovery.sh
│   ├── 06_validate.sql
│   └── execute_full.sh
├── data/                  # volume do PGDATA
├── wal_archive/           # WAL arquivado
└── base_backup/           # base backups
```

**Fluxo resumido:**
1. `01_prepare.sh` sobe o ambiente e prepara a configuração (`wal_level`, `archive_mode`, `archive_command`).
2. `02_base_backup.sh` cria o backup base em `base_backup/`.
3. `03_generate_data.sql` gera dados de teste (marco temporal para o PITR).
4. `04_simulate_error.sql` simula um erro/perda de dados.
5. `05_pitr_recovery.sh` restaura o backup base e reaplica os WALs de `wal_archive/` até o `recovery_target` escolhido.
6. `06_validate.sql` valida se os dados foram recuperados corretamente.


| Caminho | Tipo | Descrição |
|---|---|---|
| `docker-compose.yml` | Arquivo | Orquestra o container do PostgreSQL |
| `config/postgresql.conf` | Arquivo | Configurações do servidor (WAL, archiving, etc.) |
| `config/pg_hba.conf` | Arquivo | Regras de autenticação/conexão |
| `scripts/01_prepare.sh` | Script | Prepara o ambiente para o laboratório |
| `scripts/02_base_backup.sh` | Script | Gera o base backup |
| `scripts/03_generate_data.sql` | Script | Gera dados de teste |
| `scripts/04_simulate_error.sql` | Script | Simula erro/perda de dados |
| `scripts/05_pitr_recovery.sh` | Script | Executa a recuperação PITR |
| `scripts/06_validate.sql` | Script | Valida os dados após a recuperação |
| `scripts/execute_full.sh` | Script | Executa todo o fluxo do laboratório de ponta a ponta |
| `base_backup/` | Volume | Base backups gerados |
| `wal_archive/` | Volume | WALs arquivados via `archive_command` |
| `data/` | Volume | PGDATA do PostgreSQL |

## Checklist de configuração (`postgresql.conf`)

| Item | Status | Observação |
|---|---|---|
| `wal_level = replica` | OK | Necessário para PITR |
| `archive_mode = on` | OK | Já configurado |
| `archive_command` | OK | Copia para `/var/lib/postgresql/wal_archive` |
| Volume `wal_archive` | OK | Persistente |
| `pg_hba.conf` | OK | Permite conexões |

## Detalhes complementares

### Testar diferentes targets de recovery
- `recovery_target_time`
- `recovery_target_xid`
- `recovery_target_name` (usado junto com `pg_create_restore_point()`)

### Criar restore points nomeados
Útil para demonstrações e marcos de recuperação:
```sql
SELECT pg_create_restore_point('antes_do_erro');
```

### Verificar se os WALs estão sendo arquivados
```bash
ls -lh wal_archive/
```

### Forçar um checkpoint antes de anotar o timestamp (opcional)
```sql
CHECKPOINT;
SELECT NOW();
```