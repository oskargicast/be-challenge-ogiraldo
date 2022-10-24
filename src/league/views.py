from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Competition, Team, Player
from .serializers import (
    CompetitionSerializer,
    PlayerSerializer,
)


class LeagueViewSet(viewsets.ModelViewSet):

    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    lookup_field = 'code'

    @action(detail=True, methods=['post'], url_path='import')
    def import_data(self, request, code=None):
        competition = Competition.objects.retrieve_and_create(code)
        team_counter, coach_counter, player_counter = Team.objects.retrieve_and_create(competition)
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'teams_created': team_counter,
                'coaches_created': coach_counter,
                'players_created': player_counter,
                **CompetitionSerializer(competition).data
            },
        )

    @action(detail=True, methods=['get'])
    def players(self, request, code=None):
        player_qs = Player.objects.by_league(code)
        # Filters by team.
        team_name = self.request.GET.get('team_name')
        if team_name:
            player_qs = player_qs.filter(team__name__icontains=team_name)
        # Serialize queryset.
        page = self.paginate_queryset(player_qs)
        if page is not None:
            serializer = PlayerSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PlayerSerializer(player_qs, many=True)
        return Response(serializer.data)


class PlayerViewSet(viewsets.ModelViewSet):

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer