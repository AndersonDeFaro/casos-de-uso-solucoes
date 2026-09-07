
----  Criar dados de teste
CREATE TABLE IF NOT EXISTS auditoria_transacoes (
    id SERIAL PRIMARY KEY,
    descricao TEXT,
    momento_registro TIMESTAMP DEFAULT NOW()
);

INSERT INTO auditoria_transacoes (descricao) VALUES
('Registro Legítimo 1'),
('Registro Legítimo 2');

###### NO HOST
### Anote o timestamp atual
docker exec -it pg16-lab psql -U postgres -c "SELECT NOW();"

### Rotacionar novamente o WAL pra não ter problema de RECOVERY, por ser um estudo
docker exec -it pg16-lab psql -U postgres -c "SELECT pg_switch_wal();"


-------- Simular erro HUMANO
INSERT INTO auditoria_transacoes (descricao) VALUES ('Registro indesejado pós-erro');
DELETE FROM auditoria_transacoes; -- simula o erro

