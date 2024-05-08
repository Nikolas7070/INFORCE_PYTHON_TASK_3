from rest_framework import generics
from restaurant_api.results.models import DailyResults
from restaurant_api.results.serializers import DailyResultsSerializer
from datetime import date


class CurrentDayResultsAPIView(generics.ListAPIView):
    serializer_class = DailyResultsSerializer

    def get_queryset(self):
        return DailyResults.objects.filter(date=date.today())
