from django.urls import path , include
from . import views


urlpatterns = [
    path('centre/', views.hospital, name = 'centre'),
]