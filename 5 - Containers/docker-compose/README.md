### Comandos básicos

#### Subir docker compose em segundo plano
docker compose up -d 

#### Parar docker compose
docker compose down

#### Parar docker compose apagando volumes
docker compose down -v

#### Verificar composes que estão rodando
docker compose ps

#### Acompanhar Logs
docker compose logs -f

#### Construir imagem a partir de Dockerfile
docker compose build --no-cache

### Link da documentação do docker compose
https://docs.docker.com/compose/compose-file/compose-file-v3/
