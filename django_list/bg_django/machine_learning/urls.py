from django.urls import path
from . import views

# give a appName and use this name in project route as namespace
app_name = 'machine_learning_app'

# include this url list into main url file of the project
urlpatterns = [
    path('my_machine/',views.machine,name='machine')
]