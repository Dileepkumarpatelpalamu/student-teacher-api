from django.contrib import admin
from django.urls import path
from .views import StudentList,StudentDetail,TeacherList,TeacherDetail
urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<int:pk>/', StudentDetail.as_view()),
    path('teacher/', TeacherList.as_view()),
    path('teacher/<int:pk>/', TeacherDetail.as_view()),
]
