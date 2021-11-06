from django.db import models
from teacher.models import Teacher


# Create student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    reporting_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


# Create Mark model
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    term = models.CharField(max_length=20)
    subject = models.TextField(default={})
    total_marks = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)