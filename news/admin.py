from django.contrib import admin
from .models import News, Tags


# Register your models here.
class AdminNews(admin.ModelAdmin):
    list_display=('title','date',)

admin.site.register(News,AdminNews)


admin.site.register(Tags)