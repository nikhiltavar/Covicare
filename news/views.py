from django.shortcuts import render
from .models import News, Tags

def news(request):
    news = News.objects.first()
    data = {
        'news':news
    }
    return render(request, 'news/news.html', data)


