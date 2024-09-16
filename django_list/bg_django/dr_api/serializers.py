from rest_framework import serializers

class TeacherSerializer(serializers.Serializer):
    teacher_name=serializers.CharField(max_length=20)
    course_name=serializers.CharField(max_length=25)
    course_duration=serializers.IntegerField(default=0)
    seat=serializers.IntegerField(default=0)