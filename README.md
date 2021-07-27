### Projeto feito durante o curso Welcome to the Django.

# Eventex

Sistema de Eventos encomendado pela Morena.

## Como desenvolver?

1. Clone o repositório;
2. Crie um virtualenv com Python 3.8.5;
3. Ative o virtualenv;
4. Instale as dependências;
5. Configure a instância com o .env;
6. Execute os testes.

```console
git clone git@github.com/...
cd wttd
python3 -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python3 manage.py test
```

## Como fazer o deploy

1. Crie uma instância no Heroku;
2. Envie as configurações para o Heroku;
3. Defina uma SECRET_KEY segura para a instância;
4. Defina DEBUG=FALSE;
5. Configure o serviço de email;
6. Envie o código para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
```
