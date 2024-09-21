from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


"""
JWTAuthentication class in Django REST Framework (DRF) looks for the access token in the Authorization header by default.
Since the token is being stored in a cookie, DRF cannot find the token where it expects, leading to the error you’re seeing.

You need to modify the JWTAuthentication class or write a custom middleware to read the access token from the cookie rather than from the Authorization header.
"""

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        #
        # Try to get access token from cookie instead of headers
        access_token = request.COOKIES.get('access_token')
        print(access_token)
        if access_token is None:
            # If no token found in cookie, return None, meaning the request is unauthenticated
            return None

        validated_token = self.get_validated_token(access_token)
        return self.get_user(validated_token), validated_token
