from django.urls import path
from restaurant_api.restaurants.views import RestaurantCreateAPIView

urlpatterns = [
    path('restaurants/create/', RestaurantCreateAPIView.as_view(), name='restaurant_create'),
]
