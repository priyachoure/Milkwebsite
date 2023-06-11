from django.contrib import admin

# Register your models here.
from .models import product


#admin.site.register(product)


@admin.register(product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discount_price', 'category', 'product_image']
