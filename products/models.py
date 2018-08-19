from django.db import models
from django.urls import reverse


class Product(models.Model):
    name        = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"id": self.id})
