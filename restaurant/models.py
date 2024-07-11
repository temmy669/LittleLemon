from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class menu(models.Model):
    ID = models.IntegerField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(11)])
    name = models.CharField(max_length=225)
    no_of_guest = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])
    booking_date = models.DateTimeField()

class booking(models.Model):
    ID = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], primary_key=True)
    title = models.CharField(max_length=225) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])



