from rest_framework import serializers
from student.models import Student, Mark
from teacher.models import Teacher

import ast


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'gender', 'reporting_teacher']

    def validate(self, data):
        print(data)
        print(data['reporting_teacher'])
        # raise serializers.ValidationError({"reporting_teacher": "No such teacher"})
        return data


class StudentListSerializer(serializers.ModelSerializer):
    reporting_teacher = serializers.SerializerMethodField()

    def get_reporting_teacher(self, obj):
        if obj.reporting_teacher:
            return {
                "id": obj.reporting_teacher.id,
                "name": obj.reporting_teacher.name
            }
        return {}

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'gender', 'reporting_teacher']


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['id', 'student', 'term', 'subject', 'total_marks', 'created_on']

    def validate(self, data):
        subject = ast.literal_eval(data['subject'])
        sum = 0
        for i in subject.values():
            sum = sum + i
        if sum != data['total_marks']:
            raise serializers.ValidationError({"total_marks": "Issue in total mark"})
        return data


class MarkListSerializer(serializers.ModelSerializer):
    student = serializers.SerializerMethodField()

    def get_student(self,obj):
        if obj.student:
            return {
                "id": obj.student.id,
                "name": obj.student.name
            }
        return {}

    class Meta:
        model = Mark
        fields = ['id', 'student', 'term', 'subject', 'total_marks', 'created_on']