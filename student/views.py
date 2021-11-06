from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from student.serializers import StudentSerializer, StudentListSerializer, MarkSerializer, MarkListSerializer
from student.models import Student, Mark


class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer



class StudentDetail(generics.RetrieveDestroyAPIView):
    queryset = Student
    serializer_class = StudentListSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({"status": 400, "errors": {}, "message": "Something went wrong"})
        self.perform_destroy(instance)
        return Response({"status": 200, "data": {}, "message": "Deleted successfully"})


class StudentUpdate(generics.UpdateAPIView):
    queryset = Student
    serializer_class = StudentSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})


class MarkCreate(generics.CreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})


class MarkList(generics.ListAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkListSerializer


class MarkDetail(generics.RetrieveDestroyAPIView):
    queryset = Mark
    serializer_class = MarkListSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({"status": 400, "errors": {}, "message": "Something went wrong"})
        self.perform_destroy(instance)
        return Response({"status": 200, "data": {}, "message": "Deleted successfully"})


class MarkUpdate(generics.UpdateAPIView):
    queryset = Mark
    serializer_class = MarkSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})
