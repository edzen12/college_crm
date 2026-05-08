# мы должны сделать API студентов:
# получать список студентов
# искать студентов
# фильтровать по группам и курсам
# смотреть одного студента
# создавать студентов

from rest_framework import serializers
from apps.students.models import Group, Student, ContactPerson


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group 
        fields = '__all__'


class ContactPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactPerson 
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    contacts = ContactPersonSerializer(
        many=True, 
        read_only=True
    )
    group_name = serializers.CharField(
        source='group.name',
        read_only=True
    )

    class Meta:
        model = Student 
        fields = '__all__'
    
