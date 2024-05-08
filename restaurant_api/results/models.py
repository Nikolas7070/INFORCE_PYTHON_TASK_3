from django.db import models


class DailyResults(models.Model):
    # Поле для збереження результату
    date = models.DateField(auto_now_add=True)
