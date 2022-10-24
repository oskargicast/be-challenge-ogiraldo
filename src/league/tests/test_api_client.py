from django.conf import settings
from hamcrest import assert_that, equal_to, not_none
from rest_framework.test import APITestCase
from league.api_client import (
    LeagueAPIClient,
    CompetitionData,
    TeamData,
    CoachData,
    PlayerData,
)


class APIClientTestCase(APITestCase):

    def setUp(self):
        self.client = LeagueAPIClient(
            api_token=settings.API_TOKEN,
            league_code='CL',
        )

    def test_get_competitions(self):
        response = self.client.get_competitions()
        response.status_code
        assert_that(response.status_code, equal_to(200))
        data = CompetitionData(response.json()).simplify()
        assert_that(data.get('code'), equal_to('CL'))
        assert_that(data.get('name'), equal_to('UEFA Champions League'))
        assert_that(data.get('area'), equal_to('Europe'))

    def test_get_teams(self):
        response = self.client.get_teams()
        response.status_code
        assert_that(response.status_code, equal_to(200))
        data = response.json()
        # Validate Team structure.
        team = data['teams'][0]
        team_data = TeamData(team)
        data = team_data.simplify()
        assert_that(data.get('api_id'), not_none())
        assert_that(data.get('name'), not_none())
        assert_that(data.get('short_name'), not_none())
        assert_that(data.get('address'), not_none())
        assert_that(data.get('tla'), not_none())
        assert_that(data.get('area'), not_none())
        # Validate Coach structure.
        data = CoachData(team_data.get_coach()).simplify()
        assert_that(data.get('api_id'), not_none())
        assert_that(data.get('name'), not_none())
        assert_that(data.get('birthday'), not_none())
        assert_that(data.get('nationality'), not_none())
        # Validate Player structure.
        json_players = team_data.get_players()
        json_player = json_players[0]
        data = PlayerData(json_player).simplify()
        assert_that(data.get('api_id'), not_none())
        assert_that(data.get('name'), not_none())
        assert_that(data.get('position'), not_none())
        assert_that(data.get('birthday'), not_none())
        assert_that(data.get('nationality'), not_none())