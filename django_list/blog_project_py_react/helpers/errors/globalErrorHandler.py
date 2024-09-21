# your_app/exceptions.py

from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.response import Response
from .appError import AppError

# add this global Error handler into setting
def global_error_handler(exc, context):
    # Call REST framework's default exception handler first
    response = exception_handler(exc, context)

     # Handle AppError separately
    if isinstance(exc, AppError):
        # return exc.to_response()
        return Response(exc.to_response()[0], status=exc.status)

    # Now add custom logic
    if response is None:
        print(str(exc))
        # If the response is None, it means an unexpected error occurred.
        return Response({
            "isSuccess": False,
            "message": "An unexpected error occurred.",
            "data": None,
            "errors": {},
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

     # Handle API exceptions
    if isinstance(exc, APIException):
        response.data = {
            "isSuccess": False,
            "message": exc.detail,
            "data": None,
            "errors": {}
        }
    return response