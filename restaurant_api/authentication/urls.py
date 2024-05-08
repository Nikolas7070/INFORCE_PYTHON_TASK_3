from django.urls import path
from restaurant_api.authentication.views import TokenObtainPairView

urlpatterns = [
    path('token/obtain/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
