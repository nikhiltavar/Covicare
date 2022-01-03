from django.contrib import admin
from .models import Blog, Categary, Author



class AdminBlog(admin.ModelAdmin):
    list_display=('title','created_date', 'featured')

admin.site.register(Blog,AdminBlog)

admin.site.register(Author)
admin.site.register(Categary)