from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import Authentication, RestaurantService, MenuService, EmployeeService, VoteService

db = Database()
auth_service = Authentication(db)
restaurant_service = RestaurantService(db)
menu_service = MenuService(db)
employee_service = EmployeeService(db)
vote_service = VoteService(db)


@api_view(['POST'])
def add_user(request):
     # Реалізація додавання користувача
     pass


@api_view(['DELETE'])
def remove_user(request, user_id):
     # Реалізація видалення користувача
     pass


@api_view(['POST'])
def add_restaurant(request):
     # Реалізація додавання ресторану
     pass


@api_view(['DELETE'])
def remove_restaurant(request, restaurant_id):
     # Реалізація видалення ресторану
     pass


@api_view(['POST'])
def add_menu_item(request):
     # Реалізація додавання пункту меню
     pass


@api_view(['GET'])
def get_menu (request, restaurant_id):
     # Реалізація отримання меню ресторану
     pass


@api_view(['POST'])
def add_employee(request):
     # Реалізація додавання співробітника
     pass


@api_view(['POST'])
def add_vote(request):
     # Реалізація додавання голосу за меню
     pass
