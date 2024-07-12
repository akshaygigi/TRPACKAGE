from django.db import models

# Create your models here.


class TourPackage(models.Model):
    destination = models.CharField(max_length=100)
    image = models.CharField(max_length=2500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()  # Duration in days


