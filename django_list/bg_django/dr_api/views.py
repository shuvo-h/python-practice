from django.shortcuts import render
from django.views.decorators.http import require_POST
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView


# use class method in production to keep code organized
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from .models import Teacher
from .serializers import TeacherSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser


# combine view set to optimize code
class Teacher_Model_View_Set(viewsets.ModelViewSet):
    # List, Create, Delete, Update, Partial Update all by this two line code
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [IsAdminUser]


# mixing based
# class Teacher_List_Create(GenericAPIView,ListModelMixin,CreateModelMixin):
class Teacher_List_Create(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # no need to manually write. it is already written by ListCreateAPIView
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)

    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)



# class TeacherById_Retrive_UPDATE_DELETE(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
class TeacherById_Retrive_UPDATE_DELETE(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # no need to manually write. it is already written by RetrieveUpdateDestroyAPIView
    # def get(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)

    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)

    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)







# use this class based view in production
class TeacherViews(APIView):
    # Get all teachers
    def get(self, request):
        teachers = Teacher.objects.all()
        serialized_teachers = TeacherSerializer(teachers, many=True)
        return JsonResponse(serialized_teachers.data, safe=False)

    # Create a new teacher
    def post(self, request):
        python_data = JSONParser().parse(request)
        serializer = TeacherSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Successfully inserted data'}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# use this class based view in production
class TeacherByIdViews(APIView):
    # Get a teacher by ID
    def get(self, request, teacher_id=None):
        if teacher_id is None:
            return JsonResponse({'msg': "Teacher id is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return JsonResponse({'msg': "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

        serialized_teacher = TeacherSerializer(teacher)
        return JsonResponse(serialized_teacher.data)

    # Update a teacher by id
    def put(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return JsonResponse({'msg': "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

        python_data = JSONParser().parse(request)
        serializer = TeacherSerializer(teacher, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'msg': 'Successfully updated data'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a teacher by id
    def delete(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return JsonResponse({'msg': "Teacher not found"}, status=status.HTTP_404_NOT_FOUND)

        teacher.delete()
        return JsonResponse({'msg': 'Successfully deleted data'})



# Create your views here.
# QuerySet
@api_view(['GET'])
def getTeachers(request):
    teachersPY = Teacher.objects.all() #complex py data
    serializedTeachers = TeacherSerializer(teachersPY,many=True) #serialized dict data
    json_data = JSONRenderer().render(serializedTeachers.data) # convert to json
    return HttpResponse(json_data,content_type='application/json')

# Model instance
@api_view(['GET'])
def getTeacherById(request,teacher_id):
    if teacher_id is None:
        return HttpResponse({'msg':"Teacher id is required"},content_type='application/json')

    teachersPY = Teacher.objects.get(id=teacher_id) #complex py data
    serializedTeachers = TeacherSerializer(teachersPY,many=False) #serialized dict data
    json_data = JSONRenderer().render(serializedTeachers.data) # convert to json
    return HttpResponse(json_data,content_type='application/json')

# create a teacher
@api_view(['POST'])
@csrf_exempt
def create_teacher(request):
    python_data = JSONParser().parse(request)
    serializer = TeacherSerializer(data=python_data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'msg': 'Successfully inserted data'}, status=status.HTTP_201_CREATED)
    else:
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')


# update a teacher
@api_view(['PUT'])
@csrf_exempt
def update_teacher(request):
    json_data = request.body
    # json to stram convert
    stream = io.BytesIO(json_data)
    # stream to python data
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    existTeacher = Teacher.objects.get(id=id)
    # python to complex
    serializer = TeacherSerializer(existTeacher,data=python_data,partial=True)
    if serializer.is_valid():
        serializer.save()
        result = {'msg':'Successfully updated data'}
        json_data= JSONRenderer().render(result)
        return HttpResponse(json_data,content_type='application/json')
    else:
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')




# update a teacher
@api_view(['DELETE'])
@csrf_exempt
def delete_teacher(request):
    json_data = request.body
    # json to stram convert
    stream = io.BytesIO(json_data)
    # stream to python data
    python_data = JSONParser().parse(stream)
    id = python_data.get('id')
    existTeacher = Teacher.objects.get(id=id)
    existTeacher.delete()
    result = {'msg':'Successfully deleted data'}
    json_data = JSONRenderer().render(result)
    return HttpResponse(json_data,content_type='application/json')


