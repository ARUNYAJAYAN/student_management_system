import pandas as pd
import pdftables_api
import json

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from student.serializers import StudentSerializer, StudentListSerializer, MarkSerializer, MarkListSerializer
from student.models import Student, Mark


class StudentCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})

    def list(self, request):
        serializer = StudentListSerializer(self.get_queryset(), many=True)

        return Response({"status": 200, "data": serializer.data, "message": "Student list"})


class StudentUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, instance=self.get_object())

        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})

    def retrieve(self, request, *args, **kwargs):
        serializer = StudentListSerializer(self.get_object(), many=False)
        return Response({"status": 200, "data": serializer.data, "message": "Student Detail"})

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({"status": 400, "errors": {}, "message": "Something went wrong"})
        self.perform_destroy(instance)
        return Response({"status": 200, "data": {}, "message": "Deleted successfully"})


class MarkCreate(generics.ListCreateAPIView):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})

    def list(self, request):
        serializer = MarkListSerializer(self.get_queryset(), many=True)

        return Response({"status": 200, "data": serializer.data, "message": "Student list"})


class MarkUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mark
    serializer_class = MarkSerializer

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, instance=self.get_object())

        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})

    def retrieve(self, request, *args, **kwargs):
        serializer = MarkListSerializer(self.get_object(), many=False)
        return Response({"status": 200, "data": serializer.data, "message": "Student Detail"})

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            return Response({"status": 400, "errors": {}, "message": "Something went wrong"})
        self.perform_destroy(instance)
        return Response({"status": 200, "data": {}, "message": "Deleted successfully"})


class UploadStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        file = request.FILES['import_file']
        name = str(file)
        extension = name.rsplit('.', 1)
        if extension[1] == 'csv':
            data = pd.read_csv(file)
            payload = json.loads(data.to_json(orient='records'))

        serializer = self.get_serializer(data=payload, many=True)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})


class UploadPdfFile(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request):
        conversion = pdftables_api.Client('9rz95cvz5nzj')
        data = conversion.csv("Document-converted.pdf", "document")
        data = pd.read_csv("document.csv")
        payload = json.loads(data.to_json(orient='records'))
        serializer = self.get_serializer(data=payload, many=True)
        if not serializer.is_valid():
            return Response({"status": 400, "errors": serializer.errors, "message": "Something went wrong"})
        else:
            serializer.save()
            return Response({"status": 200, "data": serializer.data, "message": "Your details saved successfully"})



