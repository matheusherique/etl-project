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

## Making a request to sorted numbers

```shell
$ curl -X GET http://0.0.0.0:8000/api/sorted_numbers
```

### So you shall migrate

```shell
$ docker-compose run web python manage.py migrate
```

## Run test cases

```shell
$ docker-compose run web python manage.py test
```