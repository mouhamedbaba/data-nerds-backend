from django.http import HttpResponse
from django.shortcuts import render

from api.models import NavetteAeroport
from api.serializers import NavetteAeroportSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class NavetteViewSet(viewsets.ModelViewSet):
    
    queryset = NavetteAeroport.objects.all()
    serializer_class = NavetteAeroport
    
class NavetteAeroportFiltrerView(APIView):
    def get(self, request):
        depart = request.query_params.get('depart', None)
        arrivee = request.query_params.get('arrivee', None)

        if depart is None or arrivee is None:
            return Response({"message": "Veuillez fournir à la fois le départ et l'arrivée."}, status=status.HTTP_400_BAD_REQUEST)

        navettes = NavetteAeroport.objects.filter(depart=depart, arrivee=arrivee)
        serializer = NavetteAeroportSerializer(navettes, many=True)
        return Response(serializer.data)