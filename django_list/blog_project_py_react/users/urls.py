from django.urls import path
from .views import UsersListView

urlpatterns = [
    path('list', UsersListView.as_view(), name='users'),
]
