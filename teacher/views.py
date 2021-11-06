from django.shortcuts import render
from rest_framework import generics

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher
    serializer_class = TeacherSerializer
