from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from . import views

router = DefaultRouter()
router.register(r'team', views.TeamViewSet)
router.register(r'athlete/api', views.AthleteAPIViewSet)
router.register(r'athlete', views.AthleteViewSet)
router.register(r'game', views.GameViewSet)

urlpatterns = [
  url(r'', include(router.urls)),
]