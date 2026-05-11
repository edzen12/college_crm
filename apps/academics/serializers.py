from rest_framework import serializers
from apps.academics.models import Subject, Grade


class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(
        source='teacher.username',
        read_only=True
    )
    class Meta:
        model = Subject
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(
        source='student.first_name',
        read_only=True
    )
    subject_name = serializers.CharField(
         source='subject.name',
        read_only=True
    )
    teacher_name = serializers.CharField(
        source='teacher.username',
        read_only=True
    )
    class Meta:
        model = Grade
        fields = '__all__' 
        read_only_fields = ['teacher']    