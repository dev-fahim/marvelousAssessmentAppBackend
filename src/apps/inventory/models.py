from django.db import models
from project.core.apps.user_api.models import MainUser, ManagerUser

# Create your models here.


class Inventory(models.Model):
    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name='inventories')

    name = models.CharField(max_length=255)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    description = models.TextField()


class InventoryManagerConnectionBridge(models.Model):
    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name='inventory_connections')

    inventory = models.ForeignKey(to=Inventory, on_delete=models.CASCADE, related_name='managers')
    manager = models.ForeignKey(to=ManagerUser, on_delete=models.CASCADE, related_name='inventories')
