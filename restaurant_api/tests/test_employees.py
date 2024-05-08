from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class EmployeeTests(TestCase):
    def test_create_employee(self):
        url = reverse('employee_create')
        data = {'name': 'Test Employee'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
