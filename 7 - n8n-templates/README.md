# 7 - n8n-templates

Este diretório reúne exemplos de workflows n8n para automação e tratamento de dados em diferentes contextos.

## Objetivo

Facilitar a integração, transformação e análise de dados públicos e de datasets populares, utilizando fluxos automatizados e personalizáveis.

## Subdiretórios

### dados-abertos

Contém exemplos para exploração de dados públicos brasileiros, como:

- **Servidores Federais:** Scripts e templates para acessar, filtrar e analisar informações sobre servidores públicos federais (cargos, salários, lotações).
- **Despesas de Deputados Federais:** Ferramentas para consultar e visualizar os gastos dos deputados federais (diárias, passagens, serviços gráficos, etc).

O objetivo é promover transparência e controle social, facilitando o acesso e análise dos dados abertos disponibilizados pelo governo.

### kaggle-movies

Inclui workflows para tratamento e ajuste dos dados do dataset [The Movies Dataset](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset/data?select=movies_metadata.csv), disponível no Kaggle.

Principais funcionalidades:

- Conversão de campos JSON armazenados como string para objetos/arrays válidos.
- Atualização dos registros tratados em banco de dados (MongoDB).
- Remoção de duplicidades e padronização dos dados para facilitar análises futuras.

## Como Utilizar

1. Acesse o subdiretório desejado.
2. Siga as instruções do README de cada pasta para executar os workflows.
3. Personalize os fluxos conforme sua necessidade.

---

Sugestões e contribuições são bem-