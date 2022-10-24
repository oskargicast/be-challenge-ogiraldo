from rest_framework.test import APITestCase
from league.models import Competition, Team, Player, Coach


class CustomAPITestCase(APITestCase):

    def setUp(self):
        # Competition 3.
        # 3 teams.
        # 4 players.
        self.competition_1 = Competition.objects.create(
            code='ABC1',
            name='Test',
        )
        # Coach team 1.
        self.coach_a = Coach.objects.create(
            api_id=1,
            name='coach A',
        )
        # Team 1.
        self.team_1 = Team.objects.create(
            api_id=1,
            name='A',
            coach=self.coach_a,
        )
        self.team_1.competitions.add(self.competition_1)
        # Players: 3
        Player.objects.create(
            api_id=1,
            name='player A1',
            team=self.team_1,
        )
        Player.objects.create(
            api_id=2,
            name='player A2',
            team=self.team_1,
        )
        Player.objects.create(
            api_id=3,
            name='player A3',
            team=self.team_1,
        )

        # Team 2. Without coach.
        self.team_2 = Team.objects.create(
            api_id=2,
            name='B',
        )
        self.team_2.competitions.add(self.competition_1)
        # Players: 1
        Player.objects.create(
            api_id=4,
            name='player B1',
            team=self.team_2,
        )

        # Coach team 3.
        self.coach_c = Coach.objects.create(
            api_id=2,
            name='coach C',
        )
        # Team 3. Without players.
        self.team_3 = Team.objects.create(
            api_id=3,
            name='C',
            coach=self.coach_c,
        )
        self.team_3.competitions.add(self.competition_1)

        # Competition 2.
        self.competition_2 = Competition.objects.create(
            code='DE2',
            name='Test',
        )
        self.team_4 = Team.objects.create(
            api_id=4,
            name='D',
        )
        self.team_4.competitions.add(self.competition_2)
        Player.objects.create(
            api_id=5,
            name='player D1',
            team=self.team_4,
        )

        self.team_5 = Team.objects.create(
            api_id=5,
            name='E',
        )
        self.team_5.competitions.add(self.competition_2)