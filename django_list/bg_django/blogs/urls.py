from django.urls import path
from . import views

# give a appName and use this name in project route as namespace
app_name = 'blogs'

# include this url list into main url file of the project
urlpatterns = [
    path('',views.getBlogList,name='blogs'),
]