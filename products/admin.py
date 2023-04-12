from django.contrib import admin
from .models import Customer , Products , Order, OrderItem , ShippingAddress , Coupon

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Coupon)

