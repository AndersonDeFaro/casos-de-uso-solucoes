# Pentaho Data Integration

Jobs e transformações de ETL desenvolvidos no Pentaho Data Integration, também conhecido como PDI ou Spoon.

## Estrutura

- `dados/`: arquivos de entrada para os processos.
- `pipeline/`: transformações de dados.
- `jobs/`: fluxos de execução e orquestração.
- `saida/`: resultados gerados pelos jobs e pipelines.

## Como executar

Abra os arquivos no Spoon, confira conexões e caminhos de arquivos e execute as transformações antes dos jobs que as utilizam. Ajuste configurações específicas do ambiente sem sobrescrever os dados de origem.