from django.db import models


class Wine(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    case_price = models.IntegerField()
    case_size = models.IntegerField()
    varietal = models.CharField(max_length=100, default="none")
    vintage = models.IntegerField()
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)