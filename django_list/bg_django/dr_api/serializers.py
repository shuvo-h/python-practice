from rest_framework import serializers
from .models import Teacher

# using the default model's serializer
# it bydefault provide the create,update,delete method with some validation and field list
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id','teacher_name','course_name','course_duration','seat']  # list of field we want to include in serialize


"""
# manually create a serializer
class TeacherSerializer(serializers.Serializer):
    teacher_name=serializers.CharField(max_length=20)
    course_name=serializers.CharField(max_length=25)
    course_duration=serializers.IntegerField(default=0)
    seat=serializers.IntegerField(default=0)

    def create(self,validated_data):
        return Teacher.objects.create(**validated_data)

    def update(self,instance,validated_updated_data):
        instance.teacher_name = validated_updated_data.get('teacher_name',instance.teacher_name)
        instance.course_name = validated_updated_data.get('course_name',instance.course_name)
        instance.course_duration = validated_updated_data.get('course_duration',instance.course_duration)
        instance.seat = validated_updated_data.get('seat',instance.seat)

        instance.save()
        return instance
"""