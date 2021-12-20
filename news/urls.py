from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news),
    path('',views.index),
]
