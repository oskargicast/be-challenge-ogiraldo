from django.urls import reverse
from hamcrest import assert_that, equal_to, not_none
from rest_framework import status
from rest_framework.test import APITestCase
from league.models import Competition


class LeagueTestCase(APITestCase):
    """
    Tests league/<league_code>/import/
    """

    def test_import_data(self):
        league_code = 'CL'
        self.url = reverse(
            'leagues-import-data',
            kwargs={'league_code': league_code}
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
            competition.teams.exists().exists(),
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