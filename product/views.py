from django.shortcuts import render
from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'MyStore - Главная'
    }
    return render(request, 'product/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'product/contacts.html', context)


def category(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Категории Товаров'
    }
    return render(request, 'product/category.html', context)


def category_products(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': f'Товары категории {category_item.name}'
    }
    return render(request, 'product/product.html', context)


def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
        'title': f'{product_item.name}'
    }
    return render(request, 'product/product.html', context)
