from django.shortcuts import render
import requests


def index(request):

    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"code":"in","format":"json"}

    headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "8200d19c55msh37593ee279e19c7p122d33jsna7c4444144f1"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()  
    trackerData = data[0]
    context = {
        'tracker' : trackerData
    }

    
    return render(request, 'home.html', context)
def navabr(request):
    return render(request, 'header.html')
def footer(request):
    return render(request, 'footer.html')
def newindex(request):
    return render(request, 'index.html')