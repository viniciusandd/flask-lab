## Objetivos

Implementar uma restapi utilizando o Microframework Flask e a biblioteca Flask-RESTful.
O projeto almeja: 

- Utilizar o ambiente de desenvolvimento dentro de um container.
- Construir uma arquitetura utilizando Factorys e Blueprints.
- Manter compatibilidade com várias versões de Blueprints.
- Buscar informações de outra api (simulando um ambiente de cloud).
- Persistir suas informações em um banco de dados Postgres.
- Utilizar uma ferramenta de cachê.
- Implementar testes automatizados.
- Fazer deploy utilizando Docker e Watchtower.

## Escopo da aplicação

- A api fornece um endpoint que quando acionado consulta apis publicas e persiste seus dados.
- A api fornece endpoints para que os dados persistidos sejam consultados.

## Passo-a-passo do desenvolvimento

- Estruturar a aplicação [OK]
- Criar um ambiente de desenvolvimento e produção utilizando containers [OK]
- Definir a api que será utilizada [OK]
- Adicionar a extensão para o banco de dados (SQLAlchemy) [OK]
- Adicionar a extensão para migrações (Flask-Migrate) [OK]
- Criar as models do projeto [OK]
- Adicionar uma extensão de comandos
- Adicionar um comando para criar o banco de dados [OK]
- Criar um banco de dados (SQLITE) [OK]
- Adicionar comando para dropar e popular o banco de dados [OK]
- Criar endpoints que retornam todos os personagens e todos os episódios [OK]
- Criar endpoints que buscam personagens e episódios por id [OK]
- Adicionar um serializador para facilitar a manipulação/persistência de dados [OK]
- Adicionar os schemas (representaçãoes das models utilizada pelo serializador) [OK]
- Criar um crud completo de personagens [OK]
- Criar um crud completo de episódios [OK]
- Criar um endpoint que faz requisições http para uma api pública e persiste os dados retornados [OK]
- Executar o Postgres dentro de um container docker [OK]
- Migrar para um banco de dados Postgres [OK]
- Adicionar uma extensão de migrações de banco de dados [OK]
- Ambiente de desenvolvimento conectando no SQLITE e de produção no POSTGRES [OK]
- Simular o deploy com o watchtower
- Criar um docker-compose para subir o ambiente de desenvolvimento

## Api que será utilizada para buscar os dados

- https://rickandmortyapi.com/api/

### Rotas utilizadas

- https://rickandmortyapi.com/api/character
- https://rickandmortyapi.com/api/episode