from django.shortcuts import render
from .models import News, Tags
import requests
from django.core.paginator import Paginator

def news(request):
    url = "https://covid-19-news.p.rapidapi.com/v1/covid"
    querystring = {"q":"covid","lang":"en","page_size":"100","sort_by":"relevancy","country":"in","media":"True"}
    headers = {
    'x-rapidapi-host': "covid-19-news.p.rapidapi.com",
    'x-rapidapi-key': "8200d19c55msh37593ee279e19c7p122d33jsna7c4444144f1"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()  
    articles = data['articles']
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    finaldata = paginator.get_page(page_number)
    totalpages = finaldata.paginator.num_pages
    context = {
        'articles' : finaldata,
        'lastpage' : totalpages,
        'totalpagelist' : [n+1 for n in range(totalpages)]
    }

    return render(request, 'news/news_full.html', context)




