from django.db import models


class Wine(models.Model):

    VINTAGE_CHOICES = [(2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015),
                       (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)]

    SIZE_CHOICES = [('375mL', '375mL'), ('750mL', '750mL'), ('1.5L', '1.5L')]

    CASE_SIZE_CHOICES = [(6, 6), (12, 12)]

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=5,
                            choices=SIZE_CHOICES,
                            default="750mL")
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=50, default='Italy')
    case_price = models.PositiveIntegerField()
    case_size = models.IntegerField(choices=CASE_SIZE_CHOICES, default=12)
    varietal = models.CharField(max_length=100, default="none")
    vintage = models.IntegerField(choices=VINTAGE_CHOICES, default=2015)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)