from django.contrib.auth import get_user_model, authenticate
from .models import Account
from django.contrib.auth.models import User


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(write_only=True)
    

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "email"
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def get_fields(self):
        fields =  super().get_fields()

        print(fields, "from serializer fields")
        fields['username'].read_only = True
        fields['email'].read_only = True
        return fields
    
class AccountSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Account
        fields = ["id","description", "city", "user", "phone", "leetcode_link", "image"]
        depth  =  1


    def create(self, validated_data):
        user_data = validated_data.pop('user')
        print(user_data, "user_data", validated_data,"validated_data")
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        try:
            account,created = Account.objects.get_or_create(user = user, 
                                                            description = validated_data.pop('description'),
                                                            city = validated_data.pop('city'),
                                                            phone = validated_data.pop('phone'),
                                                            leetcode_link = validated_data.pop('leetcode_link'),
                                                            image = validated_data.pop('image'))
        
        except Exception as e:
            user.delete()
            raise

        account.user = user

        return account
    
    def update(self, instance, validated_data):

        user_data = validated_data.pop('user', {})
        user = instance.user

        data = UserSerializer(instance=user, data=user_data)

        if data.is_valid():
            data.save()

        instance.description = validated_data.get('description', instance.description)
        instance.city = validated_data.get('city', instance.city)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.leetcode_link = validated_data.get('leetcode_link', instance.leetcode_link)
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        return instance
