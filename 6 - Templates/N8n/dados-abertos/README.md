# Workflows n8n para Dados Abertos

Workflows para consultar e organizar informações públicas sobre servidores federais, deputados e despesas parlamentares. O conjunto combina consultas, cargas paginadas e fluxos de apoio a análises com IA.

## Arquivos disponíveis

### Servidores federais

- `dados-ai-servidor-federal.json`: consulta e preparação de dados para uso com IA.
- `orgao-servidor-federal-start.json`: ponto de entrada da carga de órgãos e servidores.
- `orgao-servidor-federal-loop.json`: processamento paginado da carga de órgãos e servidores.

### Deputados e despesas

- `ai-query-deputados.json`: consultas sobre deputados com apoio de IA.
- `ai-query-despesas-deputados.json`: consultas sobre despesas parlamentares com apoio de IA.
- `carga-despesas-deputados-federais-start.json`: ponto de entrada da carga de despesas.
- `carga-despesas-deputados-federais-loop.json`: processamento paginado das despesas.

### Fluxo de exemplo

- `ai-curiozinho-transparencia.json`: exemplo de interação sobre dados de transparência.

## Como utilizar

1. Importe o arquivo JSON no n8n.
2. Configure as credenciais e conexões requeridas pelos nós.
3. Execute primeiro os workflows com sufixo `start` e acompanhe os fluxos com sufixo `loop`.
4. Valide os registros gerados antes de agendar ou ativar uma execução recorrente.

## Fontes

Os fluxos foram preparados para trabalhar com dados públicos, incluindo informações disponibilizadas pelo Portal da Transparência e pela Câmara dos Deputados. Verifique os nós HTTP de cada workflow para confirmar endpoints, limites e formatos vigentes.
