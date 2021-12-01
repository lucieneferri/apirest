from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from .views import CoutryViewSet

router = DefaultRouter()
router.register(r"countries", CoutryViewSet)

urlpatterns = [
    path("", include(router.urls))
]