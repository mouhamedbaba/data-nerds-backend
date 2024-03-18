from django.http import HttpResponse
from django.shortcuts import render

from api.models import City, ImageUrl, NavetteAeroport
from api.serializers import CitySerializer, ImageUrlSerializer, NavetteAeroportSerializer, NavetteSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ImageUrlViewSet(viewsets.ModelViewSet):
    queryset = ImageUrl.objects.all()
    serializer_class = ImageUrlSerializer
    
from rest_framework import viewsets, status
from rest_framework.response import Response

class NavetteViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        depart = self.request.query_params.get('depart', None)
        arrivee = self.request.query_params.get('arrivee', None)
        
        if depart is None or arrivee is None:
            return NavetteAeroport.objects.none()  # Retourne une queryset vide
        
        return NavetteAeroport.objects.filter(depart=depart, arrivee=arrivee)
    
    serializer_class = NavetteSerializer

    
# class NavetteAeroportFiltrerView(APIView):
#     def get(self, request):
#         depart = request.query_params.get('depart', None)
#         arrivee = request.query_params.get('arrivee', None)

#         if depart is None or arrivee is None:
#             return Response({"message": "Veuillez fournir à la fois le départ et l'arrivée."}, status=status.HTTP_400_BAD_REQUEST)

#         navettes = NavetteAeroport.objects.filter(depart=depart, arrivee=arrivee)
#         serializer = NavetteAeroportSerializer(navettes, many=True)
#         return Response(serializer.data)
    
class CityVeiwSet(viewsets.ModelViewSet):
    
    queryset = City.objects.all()
    serializer_class = CitySerializer