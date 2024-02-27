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


### Testes unitários

Rode os testes unitários com docker, utilizando o comando abaixo:

`$ docker-compose up -d && docker-compose exec api pytest --cov=src src`
