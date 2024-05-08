from django.urls import path
from restaurant_api.employees.views import EmployeeCreateAPIView

urlpatterns = [
    path('employees/create/', EmployeeCreateAPIView.as_view(), name='employee_create'),
]
