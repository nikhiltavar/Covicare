from django.shortcuts import render
from .models import News, Tags
import requests

def news(request):
    news = News.objects.first()
    data = {
        'news':news
    }
    return render(request, 'news/news.html', data)

def apinews(request):
    url = "https://covid-19-news.p.rapidapi.com/v1/covid"
    querystring = {"q":"covid","lang":"en","sort_by":"relevancy","country":"in","media":"True"}
    headers = {
    'x-rapidapi-host': "covid-19-news.p.rapidapi.com",
    'x-rapidapi-key': "8200d19c55msh37593ee279e19c7p122d33jsna7c4444144f1"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()  
    articles = data['articles']
    context = {
        'articles' : articles
    }

    return render(request, 'news/apinews.html', context)




