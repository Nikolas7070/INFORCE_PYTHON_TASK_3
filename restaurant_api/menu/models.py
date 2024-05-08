from django.db import models
from restaurant_api.restaurants.models import Restaurant


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()
    # Додай інші поля, якщо потрібно
