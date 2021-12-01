from django.db.models import fields
from rest_framework import serializers
from .models import Country

class CountrySerializer(serializers.ModelSerializer):
    #essa classe ModelSerializer, diz para o Django como converter a instancia da classe em um arquivo JSON.
    class Meta:
        model = Country
        fields = ["id", "name","capital", "area"]