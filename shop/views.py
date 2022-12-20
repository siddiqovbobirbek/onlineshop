from django.shortcuts import render
from shop.models import Category, Brand, Product, Order, OrderItem
from users.models import CustomUser
from django.http import JsonResponse
import json, datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder


def home(request):

    data = cartData(request)
    cartItems = data['cartItems']
    
    products = Product.objects.all()
    category = Category.objects.all()
    images = Product.objects.all()
    brands = Brand.objects.all()


    context = { 
        'cartItems':cartItems,
        'products': products,
        'images': images,
        'category':category,
        'brands': brands }
    return render(request, 'home.html',context)


def sidebar(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    products = Product.objects.all()
    images = Product.objects.all()
    brands = Brand.objects.all()


    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        'products': products,
        'images': images,
        'brands': brands }
    return render(request, 'sidebar.html',context)

def products(request, pk):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.get(id=pk)
    xususiyatlar = products.xususiyatlar.all()
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems, 
        'products': products,
        'xususiyatlar':xususiyatlar,
    }
    return render(request, 'product_detail.html',context)
     

def login(request):
    category = Category.objects.all()

    context = {
        'category': category
    }
    return render(request, 'login.html', context)


def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        }
    return render(request, 'shop-cart.html',context)



def checkout(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    
    context = {
        'items':items, 
        'order':order, 
        'cartItems':cartItems,
        }
    return render(request, 'checkout.html',context)

def contact(request):
    category = Category.objects.all()
    product = Product.objects.all()

    context = {
        'category': category,
        'product': product 
    }
    return render(request, 'contact.html', context)


def search(request):
    query = request.GET['query']
    products = Product.objects.filter(name__icontains = query).all()

    context = {
        'products':products
    }

    return render(request, 'search.html', context)


def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']

	print('Action:', action)
	print('Product:', productId)

	customer = request.user
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
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        
        print(total, 'sss', order.get_cart_total)
        
        if int(total) == int(order.get_cart_total):
            print(total)
            order.complete = True
        order.save()

    else:
        print('User is not logged in...')
    return JsonResponse('Payment complete!', safe=False)


def my_account(request):
    context = {}
    return render(request, 'my-account.html', context)
