from django.shortcuts import render
from shop.models import Category, Brand, Product, ProductPhoto, Order, OrderDetail
from users.models import CustomUser
from django.http import JsonResponse
import json
from .models import * 
from .utils import cartData 


def home(request):
    category = Category.objects.all()
    brands = Brand.objects.all()
    images = ProductPhoto.objects.all()
    brand_phones = Brand.objects.filter(category__name='Phones')
    print(brand_phones)
    context = {
        'category': category,
        'brands': brands,
        'images': images,
    }
    return render(request, 'home.html',context)


def sidebar(request):
    product = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'sidebar.html',context)


def products(request):

    if request.user.is_authenticated:
        customuser = request.user.customuser
        order, created = Order.objects.get_or_create(customuser=customuser, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items':0}

    images = ProductPhoto.objects.all()
    context = {
        'images': images
    }
    return render(request, 'product_detail.html', context)


def login(request):
    category = Category.objects.all()

    context = {
        'category': category
    }
    return render(request, 'login.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderDetail.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)


def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)
