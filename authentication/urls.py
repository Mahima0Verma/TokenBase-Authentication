
from django.contrib import admin
from django.urls import path
from authapp.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/',RegisterView.as_view(),name="auth_register"),
    path('api/auth/login/',LoginView.as_view(),name="auth_login"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/detail/',DetailView.as_view(), name="detail"),
   
]
