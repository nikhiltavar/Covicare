from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from blog.models import Blog
from .utils import cookieCart

def shopHome(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items              
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']

    products1 = Product.objects.filter(covidEssentials=True)
    products2 = Product.objects.filter(equipments=True)
    products3 = Product.objects.filter(others=True)
    latest_post = Blog.objects.order_by('-created_date')[:3]


    context = { 
        'products1': products1,
        'products2': products2,
        'products3': products3,
        'cartitems': cartItems,
        'latest' : latest_post,
    }
    return render (request, 'ecommerce/shophome.html', context)



    
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
                        
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items'] 

    context = {
        'items':items, 
        'order':order,
        'cartitems': cartItems,
    }
    return render(request, 'ecommerce/checkout.html', context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context = {
        'items': items,
        'order': order,
        'cartitems': cartItems,
    }
    return render(request, 'ecommerce/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <=0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def productDetails(request, slug):
    product_slug = Product.objects.get(slug=slug)
    product = Product.objects.get(slug=slug)
    latest_products = Product.objects.order_by('-created_date')[:3]
    context = {
        'slug': slug,
        'product':product,
        'latest':latest_products,
    }
    return render(request, 'ecommerce/productdetails.html', context)

def processOrder(request):
    print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == float(order.get_cart_total):
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
		            customer=customer,
		            order=order,
		            address=data['shipping']['address'],
		            city=data['shipping']['city'],
		            state=data['shipping']['state'],
		            pincode=data['shipping']['pincode'],)
    else:
        return redirect('login')
    return JsonResponse('Payment Complete', safe=False)
