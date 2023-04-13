import datetime
from django.http import HttpRequest
from .models import  Customer


def get_customer(request: HttpRequest):
    customer = request.user
    if customer.is_anonymous:
        device = request.COOKIES.get("device")
        if device is None:
            device = request.COOKIES["device"] = str(datetime.datetime.now().timestamp())
        customer, _ = Customer.objects.get_or_create(device=device)
        
        return customer

    customer , _ = Customer.objects.get_or_create(name=customer)

    return customer