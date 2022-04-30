from django.urls import path , include
from . import views


urlpatterns = [
    path('shop/', views.shopHome, name = 'shop'),
    path('shop/checkout/', views.checkout, name = 'checkout'),
    path('shop/cart/', views.cart, name = 'cart'),
    path('shop/productdetails/<slug>/', views.productDetails, name = 'productdetails'),
    path('shop/update_item/', views.updateItem, name = 'update_item'),
    path('shop/checkout/process_order/', views.processOrder, name = 'process_order'),
    path('shop/cart/update_item/', views.updateItem, name = 'updatecart_item'),
]

