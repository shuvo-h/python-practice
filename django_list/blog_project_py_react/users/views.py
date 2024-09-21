from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.exceptions import NotFound
from helpers.errors.appError import AppError
from helpers.utils.response_sender import sendRes

class UsersListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Assuming you are fetching the logged-in user
        # user = request.user
        # raise AppError(
        #     status=402,
        #     message="Product already exists",
        #     errors={
        #         "name": "Name is required",
        #         "price": "Price must be a number"
        #     }
        # )


        # Prepare the data you want to send back in JSON format
        user_data = {
            'id': 50,
            'email': 'user.email',
            'role': 'finance'
        }
        return sendRes(status.HTTP_200_OK,user_data,"User retrived successfully")
        # return Response(user_data, status=status.HTTP_200_OK)
