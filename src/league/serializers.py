from rest_framework import serializers
from .models import Competition, Team, Player, Coach


class CompetitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Competition
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = '__all__'


class CoachSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coach
        fields = '__all__'