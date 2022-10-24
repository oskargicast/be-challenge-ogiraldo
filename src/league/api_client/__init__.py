import requests


class LeagueAPIClient:

    BASE_URL = 'https://api.football-data.org/v4/'

    def __init__(self, api_token: str, league_code: str) -> None:
        self.api_token = api_token
        self.league_code = league_code

    def _get_headers(self):
        return {
            'X-Auth-Token': self.api_token,
        }

    def get_competitions(self):
        endpoint = f'{self.BASE_URL}competitions/{self.league_code}'
        return self._make_request(endpoint)

    def get_teams(self):
        endpoint = f'{self.BASE_URL}competitions/{self.league_code}/teams'
        return self._make_request(endpoint)

    def _make_request(self, endpoint):
        return requests.get(endpoint, headers=self._get_headers())