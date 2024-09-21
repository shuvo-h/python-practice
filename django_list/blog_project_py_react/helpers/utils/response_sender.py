# your_app/utils.py

from rest_framework.response import Response

def sendRes(status=200,data=None, message="Success", is_success=True):
    return Response({
        "isSuccess": is_success,
        "message": message,
        "data": data,
        "errors": None,
    }, status=status)  # You can customize the status code as needed
