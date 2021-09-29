# ETL Project

## Start project

### Before starting the project create a .env file

```
### .env file

POSTGRES_DB=YOUR_DB_NAME
POSTGRES_USER=YOUR_DB_USERNAME
POSTGRES_PASSWORD=YOUR_DB_PASSWORD
POSTGRES_HOST=db
SECRET_KEY=YOUR_SECRET_KEY
```

### After

```shell
$ docker-compose up
```

## Run test cases

```shell
$ docker-compose run web python manage.py test
```