from django.urls import path
from restaurant_api.menu.views import MenuCreateAPIView, CurrentDayMenuAPIView

urlpatterns = [
    path('menus/create/', MenuCreateAPIView.as_view(), name='menu_create'),
    path('menus/current/', CurrentDayMenuAPIView.as_view(), name='current_day_menu'),
]
