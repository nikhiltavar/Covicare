from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model
from django.urls import reverse
from autoslug import AutoSlugField


User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Category'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='Blog_imgs')
    categories = models.ManyToManyField(Category)
    author = models.ForeignKey(Author, on_delete=models.CASCADE , default='admin')
    featured = models.BooleanField()
    slug = AutoSlugField(populate_from= 'title',   unique=True, null=True, default=None)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Blog'

  
