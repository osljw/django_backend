from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import LeaderboardViewSet

router = SimpleRouter(trailing_slash=False)
router.register('leaderboard', LeaderboardViewSet)

urlpatterns = router.urls