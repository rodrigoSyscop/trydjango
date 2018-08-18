from django.db import models

class Product(models.Model):
    name        = models.CharField(max_length=64)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=10)
