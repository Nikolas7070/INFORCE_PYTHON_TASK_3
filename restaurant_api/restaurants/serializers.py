# menu/serializers.py
from rest_framework import serializers
from restaurant_api.restaurants.models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
