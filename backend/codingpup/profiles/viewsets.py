from rest_framework.viewsets import ModelViewSet
from .models import Profile
from django.contrib.auth.models import User
from .serializers import ProfilePostSerializer,ProfileGetSerializer, UserSerializer
import pdb
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from rest_framework import permissions

class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProfileViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing profiles.
    """
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ProfilePostSerializer
        else:
            return ProfileGetSerializer
        
    def update(self, request, pk=None):

        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)

        user_data = request.data.get('user', {})

        #  let the user know that these fields cant be altered
        # if user_data.get('username') or user_data.get('email'):

        user_data.pop('username',None)
        user_data.pop('email',None)

        password = user_data.get('password',"")
        if password:
            user_data['password'] = make_password(password=password)
            
        user_instance = profile.user
        user_serializer = UserSerializer(user_instance, data=user_data, partial=True)
        
        profile.description = request.data.get('description', profile.description)
        profile.city = request.data.get('city', profile.city)
        profile.phone = request.data.get('phone', profile.phone)
        profile.leetcode_link = request.data.get('leetcode_link', profile.leetcode_link)
        profile.image = request.data.get('image', profile.image)

        profile_req_serializer = ProfilePostSerializer(profile, data=request.data, partial=True)

        if profile_req_serializer.is_valid():
            if user_serializer.is_valid():
                user_serializer.save()
            profile_instance = profile_req_serializer.update(profile, validated_data=profile_req_serializer.validated_data)
            profile_res_serializer = ProfileGetSerializer(profile_instance)
            return Response(profile_res_serializer.data)
        else:
            return Response(profile_req_serializer.errors, status= status.HTTP_400_BAD_REQUEST)


