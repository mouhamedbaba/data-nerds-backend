
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import NavetteAeroport
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class NavetteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NavetteAeroport
        fields = "__all__"
        

class NavetteAeroportSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavetteAeroport
        fields = ['id', 'depart', 'arrivee']
