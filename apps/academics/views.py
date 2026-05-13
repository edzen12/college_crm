from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.academics.models import Grade, Subject
from apps.academics.serializers import (
    SubjectSerializer, GradeSerializer
)


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.select_related('teacher')
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'], url_path='my-subjects')
    def my_subjects(self, request):
        subjects = Subject.objects.filter(teacher=request.user)
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.select_related(
        'student', 'teacher', 'subject'
    )
    serializer_class = GradeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter
    ]
    filterset_fields = [
        'student', 'subject', 'student__group'
    ]
    search_fields = [
        'student__first_name',
        'student__last_name',
    ]

    def perform_create(self, serializer):
        serializer.save(
            teacher=self.request.user
        )
