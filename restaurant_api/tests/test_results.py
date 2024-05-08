from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class ResultsTests(TestCase):
    def test_get_current_day_results(self):
        url = reverse('current_day_results')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
