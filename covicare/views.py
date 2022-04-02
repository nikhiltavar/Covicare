from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import requests
from .forms import SignUpForm



def signupUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')


    context = {"form": form}
    return render(request, 'signup.html', context)

def userProfile(request):
    pass


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

@login_required (login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')
    


def index(request):

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/country-report-iso-based/India/ind"

    # querystring = {"country":"india","format":"json"}

    headers = {
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com",
    'x-rapidapi-key': "8200d19c55msh37593ee279e19c7p122d33jsna7c4444144f1"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()  
   
    trackerData = data[0]

    context = {
        'tracker' : trackerData,
    }

    
    return render(request, 'home.html', context)
def navabr(request):
    return render(request, 'header.html')
def footer(request):
    return render(request, 'footer.html')

