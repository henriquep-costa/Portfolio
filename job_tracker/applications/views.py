from django.shortcuts import render
from rest_framework import viewsets
from .models import Application
# importa serializer 
from .serializers import ApplicationSerializer

# ViewSet = conjunto de ações da API
class ApplicationViewSet(viewsets.ModelViewSet):

    # queryset define quais dados serão mostrados
    # Application.objects.all() -> pega todos registros
    queryset = Application.objects.all()

    # serializer usado para transformar dados em JSON
    serializer_class = ApplicationSerializer

