from rest_framework import generics
from restaurant_api.menu.models import Menu
from restaurant_api.menu.serializers import MenuSerializer
from datetime import date


class MenuCreateAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CurrentDayMenuAPIView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        return Menu.objects.filter(date=date.today())
