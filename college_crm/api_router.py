from rest_framework.routers import DefaultRouter
from apps.accounts.views import UserViewSet
from apps.academics.views import SubjectViewSet, GradeViewSet
from apps.students.views import (
    GroupViewSet, StudentViewSet, ContactPersonViewSet
)

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('subjects', SubjectViewSet, basename='subjects')
router.register('grades', GradeViewSet, basename='grades')
router.register('groups', GroupViewSet, basename='groups')
router.register('students', StudentViewSet, basename='students')
router.register('contacts', ContactPersonViewSet, basename='contacts')

