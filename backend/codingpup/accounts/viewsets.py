from rest_framework.viewsets import ModelViewSet
from .models import Account
from django.contrib.auth.models import User
from .serializers import AccountPostSerializer,AccountGetSerializer, UserSerializer
import pdb
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer    

class AccountViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AccountPostSerializer
        else:
            return AccountGetSerializer
        
    def update(self, request, pk=None):

        try:
            account = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

        user_data = request.data.get('user', {})

        #  let the user know that these fields cant be altered
        # if user_data.get('username') or user_data.get('email'):

        user_data.pop('username',None)
        user_data.pop('email',None)

        password = user_data.get('password',"")
        if password:
            user_data['password'] = make_password(password=password)
            
        user_instance = account.user
        user_serializer = UserSerializer(user_instance, data=user_data, partial=True)
        
        account.description = request.data.get('description', account.description)
        account.city = request.data.get('city', account.city)
        account.phone = request.data.get('phone', account.phone)
        account.leetcode_link = request.data.get('leetcode_link', account.leetcode_link)
        account.image = request.data.get('image', account.image)

        account_req_serializer = AccountPostSerializer(account, data=request.data, partial=True)

        if account_req_serializer.is_valid():
            if user_serializer.is_valid():
                user_serializer.save()
            account_instance = account_req_serializer.update(account, validated_data=account_req_serializer.validated_data)
            account_res_serializer = AccountGetSerializer(account_instance)
            return Response(account_res_serializer.data)
        else:
            return Response(account_req_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
