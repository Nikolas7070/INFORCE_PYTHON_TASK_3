# menu/tests.py
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant_api.restaurants.models import Restaurant


class MenuTests(TestCase):
    def test_create_menu(self):
        url = reverse('menu_create')
        # Cnствори ресторан для зв'зяку з меню
        restaurant = Restaurant.objects.create(name='Test Restaurant')
        data = {'restaurant': restaurant.id,
                'date': '2024-05-08'}  # Дата должна быть сегодняшней или изменить логику в представлении
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_current_day_menu(self):
        url = reverse('current_day_menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
