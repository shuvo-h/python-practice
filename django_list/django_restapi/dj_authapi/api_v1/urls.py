from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    # without cookies
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    # path('test/', views.testEndPoint, name='test'),
    path('test/', views.TestEndPoint.as_view(), name='test'),
    path('', views.getRoutes),

    # with cookies
    path('cookies/token/', views.TokenCookieView.as_view(), name='token_obtain_pair'),
    path('cookies/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('cookies/token/logout/', views.LogoutView.as_view(), name='logout'),
]