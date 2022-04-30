from django.contrib import admin
from .models import *
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display=('name','slug')

admin.site.register(Customer)
admin.site.register(Product,AdminProduct)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)