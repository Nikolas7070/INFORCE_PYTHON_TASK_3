# employee/views.py
from rest_framework import generics
from restaurant_api.employees.models import Employee
from restaurant_api.employees.serializers import EmployeeSerializer


class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
