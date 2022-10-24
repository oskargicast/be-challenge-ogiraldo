from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Competition


class LeagueViewSet(viewsets.GenericViewSet):
    lookup_field = 'league_code'

    @action(detail=True, methods=['post'], url_path='import')
    def import_data(self, request, league_code=None):
        Competition.retrieve_and_create(league_code)
        # TODO: Create QuerySet manager in Team model that retrieves
        # and creates teams, coachs and players.
        return Response(
            status=status.HTTP_201_CREATED,
        )