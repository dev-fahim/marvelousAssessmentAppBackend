from django.contrib import admin
from apps.product.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'inventory',
        'added',
        'updated'
    )


admin.site.register(Product, ProductAdmin)
