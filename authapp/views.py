from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import *


# Create your views here.



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
          
            return Response({
                "message": "User registered successfully",
              
            }, status=201)  # 201 Created
        return Response(serializer.errors, status=400)  


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
            
            response=Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
               
            })
        

  
            # Set cookies
            response.set_cookie(
                'refresh_token',
                str(refresh),
                httponly=True,
                samesite='Lax',
                secure=True, 
                max_age= 7 * 24 * 60 * 60  # 7 days
            )
            response.set_cookie(
                'access_token',
                str(refresh.access_token),
                httponly=True,
                samesite='Lax',
                secure=True, 
                max_age=60   # 1 minute
            )

            return response

        else:
            return Response({'detail': 'Invalid credentials'}, status=401)





class DetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        user_serializer = UserSerializer(user)
        return Response({
            'message': 'Welcome to Page',
            'user':user_serializer.data
        }, 200

        )
