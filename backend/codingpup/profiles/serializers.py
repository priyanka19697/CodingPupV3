from django.contrib.auth import get_user_model, authenticate
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
import pdb
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email",
            "blogs",
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
    

class ProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = "__all__"
        depth = 1

class ProfilePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"
        depth = 1

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


