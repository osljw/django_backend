from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import FilterView, TravelViewSet, OrderViewSet

router = SimpleRouter(trailing_slash=True)
router.register(r'travel', TravelViewSet, basename='travel')

print("-------------router.urls:", router.urls)
urlpatterns = router.urls


urlpatterns += [
    path('travel/filter', FilterView.as_view()),
]

router = SimpleRouter()
router.register(r'order', OrderViewSet, basename='order')
urlpatterns += router.urls