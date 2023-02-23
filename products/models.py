from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    inventory_quanity = models.IntegerField()
