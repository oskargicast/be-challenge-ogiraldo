from django.urls import reverse
from hamcrest import assert_that, equal_to, not_none
from rest_framework import status
from league.models import Competition
from league.tests.utils import CustomAPITestCase


class LeagueTestCase(CustomAPITestCase):

    def test_get_competition_detail(self):
        """
        Tests leagues/
        """
        self.url = reverse(
            'leagues-detail',
            kwargs={'code': self.competition_1.code}
        )
        response = self.client.get(self.url)
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['code'], equal_to(self.competition_1.code))

    def test_import_data(self):
        """
        Tests leagues/<league_code>/import/
        """
        league_code = 'CL'
        self.url = reverse(
            'leagues-import-data',
            kwargs={'code': league_code}
        )
        response = self.client.post(self.url)
        assert_that(response.status_code, equal_to(status.HTTP_201_CREATED))
        # Checks Competitions exist with the league_code.
        competition_qs = Competition.objects.filter(code=league_code)
        assert_that(
            competition_qs.exists(),
            equal_to(True),
        )
        # Checks Teams exist with the league_code.
        competition = competition_qs.first()
        assert_that(
            competition.teams.exists(),
            equal_to(True),
        )
        # Checks Coach exists with the league_code.
        team = competition.teams.first()
        coach = team.coach
        assert_that(
            coach,
            not_none(),
        )
        # Checks Players exist with the league_code.
        assert_that(
            team.players.exists(),
            not_none(),
        )

    def test_get_players_by_league_code(self):
        """
        Tests leagues/<league_code>/players/

        Players by team:
        team A1: 3
        team A2: 1
        team A3: 0  # Only a coach.
        """
        self.url = reverse(
            'leagues-players',
            kwargs={'code': self.competition_1.code}
        )
        response = self.client.get(self.url)
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(4))

    def test_get_players_by_league_code_and_team_name(self):
        """
        Tests league/<league_code>/players/?team_name={}

        Players by team:
        team A1: 3
        team A2: 1
        team A3: 0  # Only a coach.
        """
        self.url = reverse(
            'leagues-players',
            kwargs={'code': self.competition_1.code}
        )
        # Seach in team A1.
        response = self.client.get(
            f'{self.url}?team_name={self.team_1.name}',
        )
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(3))
        # Seach in team A2.
        response = self.client.get(
            f'{self.url}?team_name={self.team_2.name}',
        )
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(1))
        # Seach in team A3.
        response = self.client.get(
            f'{self.url}?team_name={self.team_3.name}',
        )
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(0))


class TeamTestCase(CustomAPITestCase):

    def test_get_teams(self):
        """
        Tests teams/
        """
        # All the players.
        self.url = reverse('teams-list')
        response = self.client.get(self.url)
        # One extra player for other team.
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(5))

    def test_get_detail_team(self):
        """
        Tests teams/{team_id}/
        """
        # All the players.
        self.url = reverse(
            'teams-detail',
            kwargs={'pk': self.team_1.pk}
        )
        response = self.client.get(self.url)
        # One extra player for other team.
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))

    def test_get_teams_by_name(self):
        """
        Tests teams/?name={}
        """
        # All the players.
        self.url = reverse('teams-list')
        response = self.client.get(
            f'{self.url}?name={self.team_1.name}'
        )
        # One extra player for other team.
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(
            response.json()['results'][0]['name'],
            equal_to(self.team_1.name),
        )

    def test_get_players_by_detail_team(self):
        """
        Tests teams/{team_id}/players/
        """
        # Get players. Team 1.
        self.url = reverse(
            'teams-players',
            kwargs={'pk': self.team_1.pk}
        )
        response = self.client.get(self.url)
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(len(response.json()), equal_to(3))
        # Get coach if players does not exists. Team 3.
        self.url = reverse(
            'teams-players',
            kwargs={'pk': self.team_3.pk}
        )
        response = self.client.get(self.url)
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()[0]['name'], equal_to(self.team_3.coach.name))


class PlayerTestCase(CustomAPITestCase):

    def test_get_players(self):
        """
        Tests players/
        """
        # All the players.
        self.url = reverse('players-list')
        response = self.client.get(self.url)
        # One extra player for other team.
        assert_that(response.json()['count'], equal_to(5))

    def test_get_players_by_team(self):
        """
        Tests players/?team={}
        """
        # Get players. Team 1.
        self.url = reverse('players-list')
        response = self.client.get(
            f'{self.url}?team={self.team_1.pk}'
        )
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(3))
        # Get coach if players does not exists. Team 3.
        self.url = reverse('players-list')
        response = self.client.get(
            f'{self.url}?team={self.team_3.pk}'
        )
        assert_that(response.status_code, equal_to(status.HTTP_200_OK))
        assert_that(response.json()['count'], equal_to(1))