from django.contrib import admin

# Register your models here.
from .models import Product, Country, Town, StockCard


class StockCardAdmin(admin.ModelAdmin):
    pass

admin.site.register(StockCard, StockCardAdmin)
admin.site.register(Country)
admin.site.register(Town)
admin.site.register(Product)
