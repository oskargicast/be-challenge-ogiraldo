from django.contrib import admin
from .models import *


@admin.register(Competition)
class CompetitionAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'code',
        'name',
        'area',
    ]
    search_fields = [
        'id',
        'code',
        'name',
    ]


class PlayerInline(admin.TabularInline):
    model = Player
    extra = 0


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        PlayerInline,
    ]
    list_display = [
        'id',
        'api_id',
        'name',
        'short_name',
        'address',
        'tla',
        'area',
        'coach',
        'n_competitions',
    ]
    search_fields = [
        'id',
        'api_id',
        'name',
        'short_name',
    ]
    raw_id_fields = [
        'coach',
    ]

    def n_competitions(self, obj):
        return obj.competitions.all().count()


class TeamInline(admin.TabularInline):
    model = Team
    extra = 0


@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    inlines = [
        TeamInline,
    ]
    list_display = [
        'id',
        'api_id',
        'name',
        'birthday',
        'nationality',
    ]
    search_fields = [
        'id',
        'api_id',
        'name',
    ]


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'api_id',
        'name',
        'team',
        'position',
        'birthday',
        'nationality',
    ]
    search_fields = [
        'id',
        'api_id',
        'name',
    ]
    list_filter = [
        'position',
    ]
    raw_id_fields = [
        'team',
    ]