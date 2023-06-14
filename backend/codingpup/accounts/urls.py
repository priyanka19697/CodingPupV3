from django.urls import path

from rest_framework.routers import DefaultRouter
from .viewsets import AccountViewSet, UserViewSet

app_name = "accounts"

router = DefaultRouter()
router.register(r'accounts', AccountViewSet, basename='accounts')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [] + router.urls


