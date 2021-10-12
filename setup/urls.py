from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from school.views import StudentsViewSet, CoursesViewSet

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='students')
router.register('courses', CoursesViewSet, basename='courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
