from django.shortcuts import render, redirect 
from django.http import HttpResponse  
from django.http import JsonResponse
import json  
import datetime 

from store.models import * 
from django.contrib.auth.forms import UserCreationForm

from store.utils import cookieCart, cartData, guestOrder  

import sqlite3 

from django.views.generic import View

# Create home view
def home(request): 
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']


    products = Product.objects.all()
    
    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'home.html', context)

# Create contact view
def contact(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'contact.html', context)

# Create service view
def service(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'checkout.html', context)

# Create food view
def food(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()

    context = {  
        'products': products, 'cartItems': cartItems, 'order': order, 'items': items  
        }

    return render(request, 'foods.html', context) 

# Create product view
def product(request):
    name = request.GET.get('product','')
    products = list(Product.objects.filter(name=name).values())
    data = dict()
    data['products'] = products
    
    return render(request, 'foods.html', data)            

# Create home view
def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'cart.html', context)

# Create checkout view
def checkout(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)
    
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)




    