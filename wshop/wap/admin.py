from django.contrib import admin
from .models import *

#Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "code", "name", "product", "price", "available", "blocked"
    )

# class StockAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Product, ProductAdmin)
