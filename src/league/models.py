from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from league.api_client import (
    LeagueAPIClient,
    CompetitionData,
    TeamData,
    CoachData,
    PlayerData,
)


class Competition(TimeStampedModel):
    code = models.CharField(
        max_length=20,
        unique=True,
    )
    name = models.CharField(
        max_length=200,
        blank=True,
    )
    area = models.CharField(
        max_length=50,
        blank=True,
    )

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        ordering = ['-created']

    @classmethod
    def retrieve_and_create(cls, league_code):
        client = LeagueAPIClient(
            api_token=settings.API_TOKEN,
            league_code=league_code,
        )
        response = client.get_competitions()
        if response.status_code != 200:
            raise Exception(f'Could not retrieve league {league_code}')
        data = CompetitionData(response.json()).simplify()
        return Competition.objects.create(**data)


class Team(TimeStampedModel):
    api_id = models.IntegerField(
        unique=True,
    )
    name = models.CharField(
        max_length=200,
        blank=True,
    )
    short_name = models.CharField(
        max_length=100,
        blank=True,
    )
    address = models.CharField(
        max_length=300,
        blank=True,
    )
    tla = models.CharField(
        max_length=20,
        blank=True,
    )
    area = models.CharField(
        max_length=50,
        blank=True,
    )
    competitions = models.ManyToManyField(
        Competition,
        related_name='teams',
    )
    coach = models.OneToOneField(
        'league.Coach',
        related_name='coach',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'{self.id}.{self.name} - {self.api_id}'

    class Meta:
        ordering = ['-created']


class Person(TimeStampedModel):
    api_id = models.IntegerField(
        unique=True,
    )
    name = models.CharField(
        max_length=200,
        blank=True,
    )
    birthday = models.DateField(blank=True, null=True)
    nationality = models.CharField(
        max_length=200,
        blank=True,
    )

    def __str__(self):
        return f'{self.id}.{self.name} - {self.api_id}'

    class Meta:
        abstract = True


class Coach(Person):
    class Meta:
        ordering = ['-created']


class Player(Person):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name='players',
    )
    position = models.CharField(
        max_length=100,
        blank=True,
    )


    def __str__(self):
        return f'{self.id}.{self.name} - {self.api_id}'

    class Meta:
        ordering = ['-created']