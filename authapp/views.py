from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import *


# Create your views here.



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    Permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer    

    def post(self, request, *args, **kwargs):
        identifier = request.data.get('identifier')  # Get the identifier (username or email)
        password = request.data.get('password')
        
        # Try to find the user by username or email
        try:
            user = User.objects.get(username=identifier)  # Try to get user by username
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=identifier)  # Try to get user by email
            except User.DoesNotExist:
                return Response({'detail': 'Invalid credentials'}, status=401)

        # Authenticate the user
        if user.check_password(password):  # Check if the password is correct
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_serializer.data
            })
        else:
            return Response({'detail': 'Invalid credentials'}, status=401)





class DashboardView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({
            'message': 'Welcome to Page',
            'user':user_serializer.data
        }, 200

        )
