from django.urls import path, include
from . import views
from .views import TeacherViews, TeacherByIdViews
from rest_framework.routers import DefaultRouter

app_name = 'dr_api'

# create router object
router = DefaultRouter()

# regiter the router with url
router.register('',views.Teacher_Model_View_Set,basename='teacher')

# include this url list into main url file of the project
urlpatterns = [
    # view set way(get,post,put,delete,patch) all in one
    path('',include(router.urls)),

    # mixin way
    # path('list', views.Teacher_List_Create.as_view(), name='teacher-list-mixin'),
    # path('list/<int:pk>', views.TeacherById_Retrive_UPDATE_DELETE.as_view()),

    # class way
    # path('', TeacherViews.as_view(), name='teacher-list'),  # for GET all teachers and POST
    # path('<int:teacher_id>/', TeacherByIdViews.as_view(), name='teacher-detail'),  # for GET, PUT, DELETE

    # individual way
    # path('',views.getTeachers,name='teachers'),
    # path('<int:teacher_id>',views.getTeacherById,name='teachers'),
    # path('teacher/create',views.create_teacher,name='create_teacher'),
    # path('teacher/update',views.update_teacher,name='update_teacher'),
    # path('teacher/delete',views.delete_teacher,name='delete_teacher'),
]