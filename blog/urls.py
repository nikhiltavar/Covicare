from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name = 'blog'),
    path('blog/post/<slug>/', views.post, name = 'post-detail'),
    path('search/', views.blogSearch, name='search'),
    
]
