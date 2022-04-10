from django.shortcuts import render

def shopHome(request):

    
    context = {}
    return render (request, 'ecommerce/shophome.html', context)


def checkout(request):
    context = {}
    return render(request, 'ecommerce/checkout.html', context)


def cart(request):
    context = {}
    return render(request, 'ecommerce/cart.html', context)


