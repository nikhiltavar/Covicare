from django.shortcuts import render
from django.http import HttpResponse

def news(request):
    return render(request, 'news/news.html')

def index(request):
    return render(request, 'news/navbar.html')
# Create your views here.
