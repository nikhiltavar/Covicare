from django.shortcuts import render

def shopHome(request):
    return render (request, 'ecommerce/shophome.html')
