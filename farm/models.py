from django.db import models
from django.conf import settings

class Farm(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farms')

    def __str__(self):
        return self.name

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    planting_date = models.DateField()
    harvest_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='crops')

    def __str__(self):
        return self.name
class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    birth_date = models.DateField()
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='animals')

    def __str__(self):
        return self.name
