# Santex Challenge

![workflow](https://github.com/oskargicast/be-challenge-ogiraldo/actions/workflows/main.yml/badge.svg)

I will be using Django + DRF because it is a small project without extreme constraints.
We also are going to use PostgreSQL because it will be the most realistic solution for a production project.

In the future, I would use async tasks in order to proccess the import tje league data.
Perhaps Celery + Redis will be a quick and reliable way to do this.

## TODO List

- [x] 1. Setup base project.
    - [x] Docker config files.
    - [x] Django DB settings.
- [x] 2. Create football-data API client.
- [x] 3. Create models.
- [x] 4. Expose models via admin.
- [x] 5. Create import action.
    - [x] Create tests.
- [x] 6. Create API resources to retrieve data.
    - [x] Players.
    - [x] Team.
    - [x] Players of a team.

## Running the project

Building the image.
```bash
docker compose build
```

Running the migrations.
```bash
docker compose run --rm app python manage.py migrate
```

Running a local web server.
```bash
docker compose up
// Or:
docker compose run --rm --service-ports app python manage.py runserver 0.0.0.0:8000
```

Creating a django user in order to access the admin.
```bash
docker compose run --rm app python manage.py creates_dummy_superuser
```

```bash
====Superuser created====
Username: admin
Password: admin
```

Enter the [admin](http://localhost:8000/admin/login/?next=/admin/) with the username and password given in the step before.

You can create a custom super user like this:
```bash
docker compose run --rm app python manage.py createsuperuser
```

## Playground with postman

In order to emulate the api, [download the postman collection](https://github.com/oskargicast/be-challenge-ogiraldo/blob/develop/resources/Challenge.postman_collection.json) and import in postman.

![Postman collection overview](https://github.com/oskargicast/be-challenge-ogiraldo/blob/develop/resources/postman.png)

# Running tests

It tests the api client connections and the api resources implemented.
```bash
docker-compose run --rm app python manage.py test
```

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)
