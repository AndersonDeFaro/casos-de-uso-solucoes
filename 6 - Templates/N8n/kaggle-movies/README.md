# Normalização do The Movies Dataset

Workflows n8n para converter campos JSON armazenados como texto no [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data), preparando as coleções para consulta e análise no MongoDB.

## Workflows

- `ajustar-json-movies-metadata-loop.json`: normaliza registros da coleção `movies_metadata` em lotes.
- `ajustar-json-movies-credits-loop.json`: normaliza dados de créditos de filmes em lotes.
- `ajustar-json-movies-keywords-loop.json`: normaliza dados de palavras-chave em lotes.

## Tratamentos realizados

Os fluxos leem documentos paginados do MongoDB, convertem campos serializados em strings para estruturas JSON e atualizam os registros tratados. Entre os campos processados estão gêneros, coleções, empresas e países de produção, idiomas, elenco e palavras-chave, conforme a coleção.

## Como executar

1. Baixe o dataset no Kaggle e carregue as coleções de origem no MongoDB.
2. Importe o workflow correspondente à coleção no n8n.
3. Configure a credencial do MongoDB e confira o nome das coleções configuradas nos nós.
4. Execute o fluxo em um ambiente de teste e valide os documentos atualizados antes de usar dados de produção.

Os workflows atualizam documentos existentes. Faça backup das coleções ou teste em uma cópia dos dados antes da execução completa.