# Santex Challenge

I will be using Django + DRF because it is a small project without extreme constraints.
We also are going to use PostgreSQL because it will be the most realistic solution for a production project.
I would like to use async tasks in order to proccess the import tje league data.
Perhaps Celery + Redis will be a quick and reliable way to do this.

## TODO List

- [x] Setup base project.
    - [x] Docker config files.
    - [x] Django DB settings.
- [ ] Create models.
- [ ] Expose models via admin.
- [ ] Create import action.
    - [ ] Create tests.
- [ ] Create API resources to retrieve data.
    - [ ] Players.
    - [ ] Team.
    - [ ] Players of a team.
- [ ] Create tests for the endpoints of the last point.
- [ ] Make async import actions.
    - [ ] Add redis and celery to our stack.

## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)