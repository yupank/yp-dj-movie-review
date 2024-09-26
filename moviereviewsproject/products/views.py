from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'products_list.html', {'products':products})
    # return HttpResponse('Hello, you are at the products')

def product_detail(request, product_id):
    return HttpResponse(f"Your are looking at the product {product_id}")

def test_table(request):
    # return HttpResponse('Hello, you are at the products')
    products_data = {'id':11, 'price':'mock data'}
    return render(request, 'products_table.html', {'products':products_data})