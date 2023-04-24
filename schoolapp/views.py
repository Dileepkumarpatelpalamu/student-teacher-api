from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission
from .models import Student, Teacher
from .serializers import StudentSerializer, TeacherSerializer
from rest_framework.authentication import BasicAuthentication


class IsCreateUpdateDeletePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if (request.method in ['POST', 'PUT', 'DELETE']) and (request.user.is_superuser or request.user.is_staff):
            return True
        return False


class StudentList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsCreateUpdateDeletePermission]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsCreateUpdateDeletePermission]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherList(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsCreateUpdateDeletePermission]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsCreateUpdateDeletePermission]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
