from django.contrib.auth import get_user_model, authenticate
from .models import Account
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
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "password"
        ]    
        extra_kwargs = {
            'password': {'write_only': True}
        }

class AccountGetSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Account
        fields = "__all__"
        depth = 1

class AccountPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = "__all__"
        depth = 1
