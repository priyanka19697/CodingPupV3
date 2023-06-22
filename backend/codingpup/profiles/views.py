from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class HomeView(APIView):
     
   permission_classes = (IsAuthenticated, )

   def get(self, request):
       
       content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
       return Response(content)


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class ChangePasswordView(generics.UpdateAPIView):
    """ 
    An endpoint for changing password
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            #check old password

            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()

            response = {
                'status': 'succcess',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []

            }

            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

