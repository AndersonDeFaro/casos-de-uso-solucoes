# Templates n8n

Coleção de workflows n8n para ingestão, consulta, transformação e enriquecimento de dados. Os arquivos JSON podem ser importados diretamente na interface do n8n e adaptados ao ambiente de destino.

## Conteúdo

- [dados-abertos](dados-abertos/): consultas e cargas relacionadas a servidores federais, deputados e despesas parlamentares.
- [kaggle-movies](kaggle-movies/): normalização de campos JSON do The Movies Dataset em MongoDB.
- `export-n8n-data.json`: exportação de workflows relacionados a dados.
- `import-n8n-workflows.json`: arquivo para importação de workflows no n8n.

## Como importar

1. Abra o n8n e acesse a área de workflows.
2. Use a opção de importar a partir de arquivo.
3. Selecione o JSON desejado neste diretório ou em um subdiretório.
4. Configure credenciais, URLs e bancos de dados do seu ambiente.
5. Revise os nós que gravam ou removem dados antes de ativar o workflow.

## Pré-requisitos

- Instância n8n disponível.
- Credenciais para as fontes de dados utilizadas por cada fluxo.
- MongoDB configurado para os workflows que persistem dados tratados.

Cada subdiretório possui detalhes sobre a finalidade e os arquivos correspondentes.