from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Menu(models.Model):
    ID = models.AutoField(primary_key=True, validators=[MinValueValidator(0), MaxValueValidator(11)])
    title = models.CharField(max_length=225) 
    price = models.DecimalField(max_digits=10, decimal_places=2, default="0.00")
    inventory = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0) 
class Booking(models.Model):
    ID = models.AutoField(validators=[MinValueValidator(0), MaxValueValidator(5)], primary_key=True)
    name = models.CharField(max_length=225, default=ID )
    no_of_guest = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)], default=1)
    booking_date = models.DateTimeField(default="YYYY/MM/DD")




