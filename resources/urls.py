from django.urls import path , include
from . import views


urlpatterns = [
    path('shop/', views.shopHome, name = 'shop'),
    path('shop/checkout/', views.checkout, name = 'checkout'),
]