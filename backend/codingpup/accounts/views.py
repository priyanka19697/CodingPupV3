from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Account
import json
from .serializers import AccountSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Create your views here.


class AccountListView(APIView):

    def get(self,request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response({"accounts":serializer.data})

    def post(self, request):

        serializer = AccountSerializer(data=request.data)

        print(serializer.initial_data, "from line 25")

        if serializer.is_valid():
            account = serializer.create(validated_data=request.data)

            print(serializer.data, "serializer data account")
            response_data = serializer.data
            response_data['account_id'] = account.id
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

class AccountDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self,request, account_id):
        print("hitting here from get")
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, account_id):
        try:
            account = Account.objects.get(pk=account_id)
        except Account.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
        
        user_data = request.data.get('user', {})
        password = user_data.get('password',"" )

        print(password)
        print(make_password(password=password))
        if password:
            user_data['password'] = make_password(password=password)

        user_instance = account.user

        user_serializer = UserSerializer(user_instance, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        
        if 'username' in user_serializer.validated_data:
            user_serializer.validated_data.pop('username')

        account.description = request.data.get('description', account.description)
        account.city = request.data.get('city', account.city)
        account.phone = request.data.get('phone', account.phone)
        account.leetcode_link = request.data.get('leetcode_link', account.leetcode_link)
        account.image = request.data.get('image', account.image)

        account_serializer = AccountSerializer(account, data=request.data, partial=True)

        if account_serializer.is_valid():
            user_serializer.save()
            account_serializer.update(account, validated_data=account_serializer.validated_data)
            return Response(account_serializer.data)
        else:
            return Response(account_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, account_id):
        print("hitting here FROM DELETE")
        try:
            account = Account.objects.get(pk=account_id)
            account.delete()
            print(account)
        except Account.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserListView(APIView):
    """
    Retrieve list of users.
    """
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users":serializer.data})