from django.urls import path
from . import views

urlpatterns = [
    
    path('checkout', views.checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('complete-purchase/', views.complete_purchase, name='complete_purchase'),
    path('order-success/', views.order_success, name='order_success'),
    path('checkout/', views.checkout, name='checkout'),
]
