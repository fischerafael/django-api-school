from rest_framework import viewsets
from school.models import Student, Course
from school.serializer import CourseSerializer, StudentSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer