from typing import Dict, Any


class CompetitionData:

    def __init__(self, json_competition: Dict[str, Any]) -> None:
        self.json_competition = json_competition
        self.league = None

    def simplify(self) -> Dict[str, Any]:
        self.league = {
            'code': self.json_competition.get('code'),
            'name': self.json_competition.get('name'),
            'area': (self.json_competition.get('area') or {}).get('name'),
        }
        return self.league


class TeamData:

    def __init__(self, json_team: Dict[str, Any]) -> None:
        self.json_team = json_team
        self.team = None

    def simplify(self) -> Dict[str, Any]:
        self.team = {
            'api_id': self.json_team.get('id'),
            'name': self.json_team.get('name'),
            'short_name': self.json_team.get('shortName'),
            'address': self.json_team.get('address'),
            'tla': self.json_team.get('tla'),
            'area': (self.json_team.get('area') or {}).get('name'),
        }
        return self.team

    def get_coach(self):
        return self.json_team.get('coach') or {}

    def get_players(self):
        return self.json_team.get('squad') or []


class CoachData:

    def __init__(self, json_coach: Dict[str, Any]) -> None:
        self.json_coach = json_coach
        self.coach = None

    def simplify(self) -> Dict[str, Any]:
        self.coach = {
            'api_id': self.json_coach.get('id'),
            'name': self.json_coach.get('name'),
            'birthday': self.json_coach.get('dateOfBirth'),
            'nationality': self.json_coach.get('nationality'),
        }
        return self.coach


class PlayerData:

    def __init__(self, json_player: Dict[str, Any]) -> None:
        self.json_player = json_player
        self.player = None

    def simplify(self) -> Dict[str, Any]:
        self.player = {
            'api_id': self.json_player.get('id'),
            'name': self.json_player.get('name'),
            'position': self.json_player.get('position'),
            'birthday': self.json_player.get('dateOfBirth'),
            'nationality': self.json_player.get('nationality'),
        }
        return self.player