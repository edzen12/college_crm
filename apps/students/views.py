from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from apps.students.models import Group, Student, ContactPerson
from apps.students.serializers import (
    GroupSerializer, StudentSerializer, ContactPersonSerializer
)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related(
        'group'
    ).prefetch_related('contacts')
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]
    filterset_fields = [
        'group', 
        'group__course'
    ]
    search_fields = [
        'first_name',
        'last_name',
        'inn',
    ]