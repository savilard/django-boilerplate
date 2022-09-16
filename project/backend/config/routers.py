from django.urls import include
from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.users.api.viewsets import UserViewSet

router = SimpleRouter()

router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls')),
    path('', include(router.urls)),
]
