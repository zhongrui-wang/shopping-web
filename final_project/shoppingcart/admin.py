from django.contrib import admin
from shoppingcart.models import Cart, Order
# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)