"""student_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import StudentCreate, StudentUpdate, MarkCreate, MarkUpdate, UploadStudent, UploadPdfFile
from teacher.views import TeacherList, TeacherDetail

urlpatterns = [
    path('api/students', StudentCreate.as_view()),
    path('api/students/<int:pk>', StudentUpdate.as_view()),
    path('api/student/marks', MarkCreate.as_view()),
    path('api/student/marks/<int:pk>', MarkUpdate.as_view()),
    path('api/teachers', TeacherList.as_view()),
    path('api/import-student', UploadStudent.as_view()),
    path('api/student', UploadPdfFile.as_view()),
    path('api/teachers/<int:pk>', TeacherDetail.as_view()),
    path('admin/', admin.site.urls),
]
