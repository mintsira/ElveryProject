from django.contrib import admin
from .models import Product, Customer, Order, OrderItem, ShippingAddress

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image', 'image_hover', 'slug', 'tag_class', 'tag']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)



admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
