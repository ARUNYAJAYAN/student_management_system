from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer


class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response({"status": 200, "data": serializer.data, "message": "Teachers list"})


class TeacherDetail(generics.RetrieveAPIView):
    queryset = Teacher
    serializer_class = TeacherSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), many=False)
        return Response({"status": 200, "data": serializer.data, "message": "Teacher's Detail"})
