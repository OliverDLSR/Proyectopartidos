from rest_framework import serializers
from .models import PartidoPolitico

class PartidoPoliticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartidoPolitico
        fields = ['id', 'nombre']
