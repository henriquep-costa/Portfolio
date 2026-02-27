from rest_framework import serializers
from .models import Application


# Classe que define como Application vira JSON
class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        # inclua todos os campos do modelo
        fields = '__all__'