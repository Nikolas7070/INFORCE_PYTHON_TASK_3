from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Restaurant


class RestaurantTests(APITestCase):
    def test_create_restaurant(self):
        url = reverse('restaurant-list')
        data = {'name': 'Test Restaurant'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Restaurant.objects.count(), 1)
        self.assertEqual(Restaurant.objects.get().name, 'Test Restaurant')
