from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from helpers.errors.appError import AppError
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

"""
JWTAuthentication class in Django REST Framework (DRF) looks for the access token in the Authorization header by default.
Since the token is being stored in a cookie, DRF cannot find the token where it expects, leading to the error you’re seeing.

You need to modify the JWTAuthentication class or write a custom middleware to read the access token from the cookie rather than from the Authorization header.
"""


class CheckAuth(JWTAuthentication):
    def get_raw_token(self, request):
        # Assuming the cookie name is 'access'
        return request.COOKIES.get('access_token')

    def get_bearer_token(self, request):
        # Extract token from the Authorization header
        auth_header = request.META.get('HTTP_AUTHORIZATION')
        if auth_header and auth_header.startswith('Bearer '):
            return auth_header.split(' ')[1]
        return None

    def authenticate(self, request):
        raw_token = self.get_raw_token(request)
        if raw_token is None:
            raw_token = self.get_bearer_token(request)

        print('raw_token = ',raw_token)
        if raw_token is None:
            raise AppError(401,"You are unauthorized",)

        try:
            validated_token = self.get_validated_token(raw_token)
        except AuthenticationFailed:
            raise AppError(401,"Invalid token",)

        user = self.get_user(validated_token)
        return (user, validated_token)


def get_role_permission(*allowed_roles):
    return RoleBasedPermission(allowed_roles=allowed_roles)


class RoleBasedPermission(BasePermission):
    def __init__(self, allowed_roles=None):
        self.allowed_roles = allowed_roles or []  # Set allowed roles from the argument

    def has_permission(self, request, view):
        user = request.user
        if not user.is_authenticated:
            return False  # User must be authenticated

        if user.role not in self.allowed_roles:
            # Raise a custom error with a message if the user has an invalid role
            # raise PermissionDenied({"detail": f"You do not have permission to access this resource. Required roles: {', '.join(self.allowed_roles)}."})
            raise AppError(401,"You are not permitted to access this resources",)

        return True
