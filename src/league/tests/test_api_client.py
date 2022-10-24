from django.conf import settings
from hamcrest import assert_that, equal_to
from league.api_client import LeagueAPIClient
from rest_framework.test import APITestCase


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

    def test_get_teams(self):
        response = self.client.get_teams()
        response.status_code
        assert_that(response.status_code, equal_to(200))