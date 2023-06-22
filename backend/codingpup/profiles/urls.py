from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .viewsets import ProfileViewSet, UserViewSet

app_name = "profiles"

urlpatterns = [
     
]
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet, basename='profiles')
router.register(r'users', UserViewSet, basename='user')

urlpatterns +=  router.urls


