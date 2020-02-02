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
- Criar um banco de dados

## Api que será utilizada para buscar os dados

- https://rickandmortyapi.com/api/

### Rotas utilizadas

- https://rickandmortyapi.com/api/characters
- https://rickandmortyapi.com/api/episodes