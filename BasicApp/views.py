from unicodedata import name
from django.shortcuts import render
from FoodApp.models import FoodItem


def Index(request):
    foodItems = FoodItem.objects.all()
    context = {
        'foodItems': foodItems,
    }
    return render(request, 'basicpages/index.html', context)


def About(request):
    return render(request, 'basicpages/about.html')


def Contact(request):
    return render(request, 'basicpages/contact.html')


def Search(request):
    return render(request, 'food/menu.html')
