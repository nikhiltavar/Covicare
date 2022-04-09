from django.shortcuts import render

def shopHome(request):
    return render (request, 'ecommerce/shophome.html')


def checkout(request):
    context = {}
    return render(request, 'ecommerce/checkout.html', context)


def cart(request):
    context = {}
    return render(request, 'ecommerce/cart.html', context)


