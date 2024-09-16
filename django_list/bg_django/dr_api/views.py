from django.shortcuts import render
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
# QuerySet
def getTeachers(request):
    teachersPY = Teacher.objects.all() #complex py data
    serializedTeachers = TeacherSerializer(teachersPY,many=True) #serialized dict data
    json_data = JSONRenderer().render(serializedTeachers.data) # convert to json
    return HttpResponse(json_data,content_type='application/json')

# Model instance
def getTeacherById(request,teacher_id):
    teachersPY = Teacher.objects.get(id=teacher_id) #complex py data
    serializedTeachers = TeacherSerializer(teachersPY,many=False) #serialized dict data
    json_data = JSONRenderer().render(serializedTeachers.data) # convert to json
    return HttpResponse(json_data,content_type='application/json')



