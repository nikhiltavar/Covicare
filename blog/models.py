from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Categary(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Categary'

class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = HTMLField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='Blog_imgs')
    categaries = models.ManyToManyField(Categary)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    featured = models.BooleanField()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Blog'
 