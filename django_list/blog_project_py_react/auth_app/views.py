from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegisterSerializer, OTPVerificationSerializer
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from helpers.utils.response_sender import sendRes
from helpers.errors.appError import AppError
from django.db import transaction

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Using transaction.atomic() to ensure rollback on errors
        with transaction.atomic():
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
        return sendRes(status.HTTP_201_CREATED,serializer.data,"User created successfully")


class VerifyOTPView(generics.GenericAPIView):
    serializer_class = OTPVerificationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Email verified successfully.'}, status=status.HTTP_200_OK)
