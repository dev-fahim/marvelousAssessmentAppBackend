from django.db import models
from project.core.apps.user_api.models import MainUser, ManagerUser

# Create your models here.


class Inventory(models.Model):
    main_user = models.ForeignKey(to=MainUser, on_delete=models.CASCADE, related_name='inventories')

    name = models.CharField(max_length=255)

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    description = models.TextField()

    managers = models.ManyToManyField(to=ManagerUser, related_name='inventories')

    objects = models.Manager()

    def __str__(self):
        return self.name
