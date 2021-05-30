# **API Exchange Currency**
___
## Tecnologias usadas:
* Python
* FastAPI
* Pytest
* Docker
____

## Como rodar o projeto usando docker
* Clone o repositório.
````console
git clone https://github.com/Sidneyasjr/exchange-currency.git
````
* Acesse a pasta.
````console
cd exchange-currency
````
* No terminal, execute o comando:
````console
docker-compose up --build
````
* Para rodar os testes:
````console
docker-compose up -d
docker-compose exec web pytest
````
* Para para teste manuais acesse: http://localhost:8000/docs
___
## Como rodar o projeto usando virtalenv
* Clone o repositório.
````console
git clone https://github.com/Sidneyasjr/exchange-currency.git
````
* Acesse a pasta.
````console
cd exchange-currency
````
* Crie um virtualenv com Python 3.9:
````console
python -m venv .venv
````
* Ativa a virtualenv:
````console
python -m venv .venv
````
* Instale as dependencias:
````console
pip install -r requirements-dev.txt
````
* Para rodar os testes:
````console
pytest
````
* Para para teste manuais acesse: http://localhost:8000/docs
___
## Documentação API
[Link documentação api](https://documenter.getpostman.com/view/16008943/TzXzEHwd#f9d267ae-ef34-4fa8-8d67-1d50a1364d47)