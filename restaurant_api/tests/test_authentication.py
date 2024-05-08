from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User


class AuthenticationTests(TestCase):
    def test_token_obtain_pair_view(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'test_user', 'password': 'test_password'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('refresh', response.data)
        self.assertIn('access', response.data)
