from rest_framework import generics
from restaurant_api.restaurants.models import Restaurant
from restaurant_api.restaurants.serializers import RestaurantSerializer


class RestaurantCreateAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
