from django.urls import path
from . import views


urlpatterns = [
    path('checkout/', views.checkout, name="CheckOut"),
    path('complete-order/', views.complete_order, name="Order_Complete"),
]