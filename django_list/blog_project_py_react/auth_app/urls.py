# projectroot/auth_app/urls.py

from django.urls import path
from .views import UserRegisterView, VerifyOTPView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
]
