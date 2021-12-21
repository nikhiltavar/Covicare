from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.news, name = 'news'),
    path('apinews/', views.apinews, name = 'apinews')
]
