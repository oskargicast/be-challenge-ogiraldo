from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from league.views import LeagueViewSet, PlayerViewSet


router = DefaultRouter()

router.register(
    r'leagues',
    LeagueViewSet,
    basename="leagues",
)
router.register(
    r'players',
    PlayerViewSet,
    basename="players",
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]