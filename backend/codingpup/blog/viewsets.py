from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import serializers, permissions

# Create your views here.

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)