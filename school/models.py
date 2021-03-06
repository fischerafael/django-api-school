from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=30)
    document = models.CharField(max_length=9)
    sex = models.CharField(max_length=11)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Course(models.Model):
    LEVEL = {
        ('B', 'BASIC'),
        ('I', 'INTERMEDIATE'),
        ('A', 'ADVANCED')
    }

    course_code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.description