from django.contrib import admin
from apps.inventory.models import Inventory

# Register your models here.


class InventoryAdmin(admin.ModelAdmin):
    list_display = (
        'main_user',
        'added',
        'updated'
    )


admin.site.register(Inventory, InventoryAdmin)
