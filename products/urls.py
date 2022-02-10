from django.urls import path
from . import views

urlpatterns = [
    path('store/', views.ProductListView.as_view(), name="Store"),
    path('products/<str:pk>', views.products, name="Products"),
    path('cart/', views.cart, name="Cart"),
    path('delete/<str:pk>/', views.delete, name="Products_Delete"),
    path('product_checkout/', views.checkout, name="Products_CheckOut"),

] 