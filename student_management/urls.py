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
from student.views import StudentList, StudentDetail, StudentCreate, StudentUpdate, \
    MarkList, MarkDetail, MarkCreate, MarkUpdate
from teacher.views import TeacherList, TeacherDetail

urlpatterns = [
    path('api/student', StudentCreate.as_view()),
    path('api/student/<int:pk>', StudentUpdate.as_view()),
    path('api/students', StudentList.as_view()),
    path('api/students/<int:pk>', StudentDetail.as_view()),
    path('api/student/mark', MarkCreate.as_view()),
    path('api/student/mark/<int:pk>', MarkUpdate.as_view()),
    path('api/student/marks', MarkList.as_view()),
    path('api/student/marks/<int:pk>', MarkDetail.as_view()),
    path('api/teachers', TeacherList.as_view()),
    path('api/teachers', TeacherDetail.as_view()),
    path('admin/', admin.site.urls),
]
