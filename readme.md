# Competition Api

Api desenvolvida em Python, teste técnico proposto pela EstanteVirtual.


### Requisitos

- Python >= 3.11
- Docker


### Utilizando Docker

Utilize [Docker](https://www.docker.com/get-started/) para rodar a api.
Execute os comandos abaixo na pasta root.

`$ docker-compose build`

`$ docker-compose up`


### Documentação

Documentação [http://localhost:8008/docs](http://localhost:8008/docs)


### Rodando localmente

#### Requisitos
- Python 3.11

Acesse a pasta do projeto e execute o comando abaixo:

`$ pip install --no-cache-dir -r requirements.txt`

`$ python src/main.py`

### Testes unitários

Acesse [GitActions](https://github.com/vanessasoutoc/competicao-api/actions)

Rode os testes unitários com docker, utilizando o comando abaixo:

`$ docker-compose up -d && docker-compose exec competicoes pytest --cov=src src`


### Banco de Dados

- SQLITE

Para limpar o banco de dados basta rodar o comando:

`$ python migrations/competicoes.py`
