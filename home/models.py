from django.db import models


class Car(models.Model):
    make = models.CharField(max_length=100)
    year = models.IntegerField()


class Bike(models.Model):
    make = models.CharField(max_length=100)
    year = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bikes')