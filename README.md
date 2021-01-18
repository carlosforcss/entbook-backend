# Welcome to entbook.
#### A simple CRUD for save companies.

### System requirements.
- Docker and docker compose.

### Local Deployment.
Put on your shell the next instructions. (You have to be on the project base folder)
1. export COMPOSE_FILE=local.yml
3. docker-compose build
2. docker-compose run app ./manage.py migrate
3. docker-compose run --service-ports app ./manage.py runserver 0.0.0.0:8000
And then the project is runing at localhost:8000.

If it's needed or you want to use the admin, you can excecute 
"docker-compose run app ./manage.py createsuperuser" for create a 
superuser.

### Production deployment.
Put on your shell the next instructions. (You have to be on the project base folder)
1. export COMPOSE_FILE=production.py
2. docker-compose up --build -d
3. docker-compose exec app ./manage.py migrate
4. docker-compose exec app ./manage.py collectstatic
4. docker-compose exec app ./manage.py createsuperuser
And then the project is runing at port 80.
   
### How to run tests.
You don't need to have the project running for test, and there are no differences
between test with production or with local configuration, but in this example
we are going to test with local configuration.
1. export COMPOSE_FILE=local.yml
2. docker-compose build (if the project is already built, ignore this.)
3. docker-compose run app ./manage.py test --nomigrations


### Project structure
#### Config
The config module works as your name says, for the project configuration.
Here are local and production django settings modules (inside config.settings) 
and config.settings.base for both environments.

#### Entbook
This package includes the most of the project. Includes the django apps
(more about django apps structure below) and utils module (which is used for
building generic tools.).
###### Entbook/compnies
Django app for evrything related to companies.
###### Entbook/companies
Python module for generics, some files are equal to a django app, and that's
because includes tools for that django module (for examples models or tests).
