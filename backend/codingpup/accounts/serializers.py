from django.contrib.auth import get_user_model, authenticate
from .models import Account
from django.contrib.auth.models import User


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "is_active",
            "is_staff",
            "is_superuser",
            "date_joined",
        ]

    # def create(self, validated_data):
    #     return get_user_model().objects.crea


class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ["description", "city", "user"]
        # extra_kwargs = {"password": {"write_only": True, "min_length": 5}}
        depth = 1
