from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.students.models import Group, Student, ContactPerson
from apps.students.serializers import (
    GroupSerializer, StudentSerializer, ContactPersonSerializer
)
from apps.academics.serializers import GradeSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def students(self, request, pk=None):
        group = self.get_object()
        students = group.students.all()
        serializer = StudentSerializer(
            students, many=True
        )
        return Response(serializer.data)


class ContactPersonViewSet(viewsets.ModelViewSet):
    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
    permission_classes = [IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related(
        'group'
    ).prefetch_related('contacts', 'grades')
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

    @action(detail=True, methods=['get'])
    def grades(self, request, pk=None):
        student = self.get_object()
        grades = student.grades.all()
        serializer = GradeSerializer(
            grades, many=True
        )
        return Response(serializer.data)