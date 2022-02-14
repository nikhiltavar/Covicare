from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog, name = 'blog'),
    path('blog/post/<slug>/', views.post, name = 'post-detail'),
    path('search/', views.blogSearch, name='search'),
    path('blog/updatepost/<slug>/', views.updatePost, name='updatepost'),
    path('blog/deletepost/<slug>/', views.deletePost, name='deletepost'),
    path('blog/createpost/', views.createPost, name='createpost'),
    path('blog/test/', views.testPost, name='testpost'),
    
]
