from django.urls import path
from . import views

app_name = 'dr_api'


# include this url list into main url file of the project
urlpatterns = [
    path('',views.getTeachers,name='teachers'),
    path('<int:teacher_id>',views.getTeacherById,name='teachers'),
]