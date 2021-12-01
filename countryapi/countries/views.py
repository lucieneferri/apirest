from django.shortcuts import render

from rest_framework import viewsets
from .models import Country
from .serializers import CountrySerializer

class CoutryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    query = Country.objects.all()
