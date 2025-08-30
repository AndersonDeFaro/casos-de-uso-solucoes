# Ajuste e Tratamento dos Dados - Movies Metadata (Kaggle)

Este diretório contém o workflow utilizado para tratar e ajustar os dados do arquivo `movies_metadata.csv` do [The Movies Dataset - Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data?select=movies_metadata.csv).

## Objetivo

O objetivo principal é corrigir e padronizar os campos do dataset que estão armazenados como strings JSON, garantindo que fiquem no formato correto para análise e manipulação no MongoDB.

## Principais etapas do workflow

- **Leitura dos dados:**  
  Os registros são lidos da coleção `movies_metadata` no MongoDB, utilizando paginação para processar em lotes.

- **Conversão de campos JSON:**  
  Os campos `genres`, `belongs_to_collection`, `production_companies`, `production_countries` e `spoken_languages` são convertidos de string para objetos/arrays JSON válidos.

- **Atualização dos registros:**  
  Após o tratamento, os registros são atualizados na coleção, substituindo os campos convertidos.

- **Remoção de duplicidades:**  
  O workflow inclui uma etapa para remover registros duplicados, garantindo a integridade dos dados.

- **Execução em loop:**  
  O processo é realizado em loop, utilizando paginação para garantir que todos os registros sejam processados.

## Estrutura dos arquivos

- **ajustar-json-movies-metadata-loop.json:**  
  Arquivo principal do workflow n8n, contendo toda a lógica de tratamento e atualização dos dados.

## Observações

- O tratamento é essencial para garantir que os campos complexos estejam em formato adequado para consultas e análises.
- O workflow pode ser adaptado para outros campos ou datasets similares.

---