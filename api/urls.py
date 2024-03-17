from django.urls import include, path

from .views import UserViewSet, NavetteAeroportFiltrerView

from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'navettes', NavetteAeroportFiltrerView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
