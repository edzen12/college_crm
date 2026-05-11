from rest_framework.routers import DefaultRouter
from django.urls import path, include
from apps.academics.views import SubjectViewSet, GradeViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet)
router.register('grades', GradeViewSet)

urlpatterns = [
    path('', include(router.urls))
]
