from rest_framework import serializers
from restaurant_api.results.models import DailyResults


class DailyResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyResults
        fields = '__all__'
