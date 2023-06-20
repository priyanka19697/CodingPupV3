from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .viewsets import BlogViewSet

app_name = 'blogs'

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blogs')

urlpatterns = []

urlpatterns += router.urls