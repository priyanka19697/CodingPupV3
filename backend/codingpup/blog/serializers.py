from .models import Blog
from rest_framework import serializers
from profiles.serializers import UserSerializer

class BlogSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.author.username
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'content', 'author', 'created_at')

