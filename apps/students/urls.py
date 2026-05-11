from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.students.views import (
    GroupViewSet, StudentViewSet, ContactPersonViewSet
)

router = DefaultRouter()

router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)
router.register('contacts', ContactPersonViewSet)

urlpatterns = [
    path('', include(router.urls))
]
