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


class CompetitionManager(models.Manager):

    def retrieve_and_create(self, league_code):
        client = LeagueAPIClient(
            api_token=settings.API_TOKEN,
            league_code=league_code,
        )
        response = client.get_competitions()
        if response.status_code != 200:
            raise Exception(f'Could not retrieve league {league_code}')
        data = CompetitionData(response.json()).simplify()
        competition, _ = Competition.objects.get_or_create(**data)
        return competition


class Competition(TimeStampedModel):
    code = models.CharField(
        max_length=20,
        unique=True,
    )
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    area = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    objects = CompetitionManager()

    def __str__(self):
        return f'{self.name} ({self.code})'

    class Meta:
        ordering = ['-created']


class TeamManager(models.Manager):

    def retrieve_and_create(self, competition):
        league_code = competition.code
        client = LeagueAPIClient(
            api_token=settings.API_TOKEN,
            league_code=league_code,
        )
        response = client.get_teams()
        if response.status_code != 200:
            raise Exception(
                f'Could not retrieve teams for league {league_code}'
            )
        json_teams = response.json().get('teams') or []
        for json_team in json_teams:
            # Creates Team.
            team_data = TeamData(json_team)
            # Creates Coach.
            coach = None
            coach_data = CoachData(team_data.get_coach())
            coach_obj = coach_data.simplify()
            if coach_obj.get('api_id'):
                coach, _ = Coach.objects.get_or_create(
                    api_id=coach_obj.get('api_id'),
                    defaults=coach_obj,
                )
            # Creates Team.
            team_obj = team_data.simplify()
            if coach:
                team_obj['coach'] = coach
            team, team_was_created = Team.objects.get_or_create(
                api_id=team_obj.get('api_id'),
                defaults=team_obj,
            )
            if team_was_created:
                team.competitions.add(competition)
            # Creates Players.
            json_players = team_data.get_players()
            for json_player in json_players:
                player_data = PlayerData(json_player)
                player_obj = player_data.simplify()
                player_obj['team'] = team
                player_api_id = player_obj.get('api_id')
                try:
                    Player.objects.get_or_create(
                        api_id=player_api_id,
                        defaults=player_obj,
                    )
                except Exception as error:
                    import ipdb; ipdb.set_trace()


class Team(TimeStampedModel):
    api_id = models.IntegerField(
        unique=True,
    )
    name = models.CharField(
        max_length=200,
        blank=True,
        null=True,
    )
    short_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=300,
        blank=True,
        null=True,
    )
    tla = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    area = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    competitions = models.ManyToManyField(
        Competition,
        related_name='teams',
    )
    coach = models.ForeignKey(
        'league.Coach',
        related_name='coach',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = TeamManager()

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
        null=True,
    )
    birthday = models.DateField(
        blank=True,
        null=True,
    )
    nationality = models.CharField(
        max_length=200,
        blank=True,
        null=True,
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
        null=True,
    )


    def __str__(self):
        return f'{self.id}.{self.name} - {self.api_id}'

    class Meta:
        ordering = ['-created']