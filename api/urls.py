from django.urls import include, path

from .views import CityVeiwSet, ImageUrlViewSet, NavetteViewSet, UserViewSet

from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'images', ImageUrlViewSet)
router.register(r'navette_aeroport', NavetteViewSet, basename='navette_aeroport')
router.register(r'cities', CityVeiwSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
