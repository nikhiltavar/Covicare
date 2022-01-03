from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
import requests

def loginUser(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username, password=password)
        except:
            messages.error(request, 'not existing user.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exists')

    return render(request, 'login-page.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


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

