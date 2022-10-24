# Santex Challenge

I will be using Django + DRF because it is a small project without extreme constraints.
We also are going to use PostgreSQL because it will be the most realistic solution for a production project.
I would like to use async tasks in order to proccess the import tje league data.
Perhaps Celery + Redis will be a quick and reliable way to do this.

## TODO List

- [x] 1. Setup base project.
    - [x] Docker config files.
    - [x] Django DB settings.
- [x] 2. Create football-data API client.
- [x] 3. Create models.
- [x] 4. Expose models via admin.
- [ ] 5. Create import action.
    - [ ] Create tests.
- [ ] 6. Create API resources to retrieve data.
    - [ ] Players.
    - [ ] Team.
    - [ ] Players of a team.
- [ ] 7. Create tests for the endpoints of the last point.
- [ ] 8. Make async import actions.
    - [ ] Add redis and celery to our stack.

## Running the project

Building the image.
```bash
docker compose build
```

Running the migrations.
```bash
docker compose run --rm app python manage.py makemigrations
docker compose run --rm app python manage.py migrate
```


```bash
docker compose up
// Or:
docker compose run --rm --service-ports app python manage.py runserver 0.0.0.0:8000
```


# Running tests

It tests api client handlers.
```bash
docker-compose run --rm app python manage.py test league.tests.test_api_client
```

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)