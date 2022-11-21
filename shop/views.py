from django.shortcuts import render
from shop.models import Category


def home_page(request):
    category = Category.objects.all()

    context = {
        'category':category,
    }
    return render(request, template_name='home.html', context=context)
