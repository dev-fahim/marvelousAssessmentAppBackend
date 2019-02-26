from django.db import models
from apps.inventory.models import Inventory

# Create your models here.


class ProductManager(models.Manager):

    def get_main_user(self):
        pass

    def get_queryset(self):
        return super()


class Product(models.Model):
    inventory = models.ForeignKey(to=Inventory, on_delete=models.CASCADE, related_name='products')

    name = models.CharField(max_length=255)
    description = models.TextField()

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
