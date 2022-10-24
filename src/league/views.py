from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Competition, Team
from .serializers import CompetitionSerializer


class LeagueViewSet(viewsets.GenericViewSet):
    lookup_field = 'league_code'

    @action(detail=True, methods=['post'], url_path='import')
    def import_data(self, request, league_code=None):
        competition = Competition.objects.retrieve_and_create(league_code)
        team_counter, couch_counter, player_counter = Team.objects.retrieve_and_create(competition)
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'teams_created': team_counter,
                'coaches_created': couch_counter,
                'players_created': player_counter,
                **CompetitionSerializer(competition).data
            },
        )