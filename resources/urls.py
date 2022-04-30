from django.urls import path , include
from . import views


urlpatterns = [
    path('centre/', views.hospital, name = 'centres'),
    path('centresearch/', views.centreSearch, name='search'),
    path('centre/centre-details/<slug>/', views.centreDetail, name = 'centre-detail'),

]