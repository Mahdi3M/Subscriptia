from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'home.html')


def product_single(request, product_id):
    return render(request, 'product_single.html', {})


def add_product(request):
    if request.method == 'POST':
        product = ProductForm(request.POST, request.FILES)
        if product.is_valid():
            product.save()
            return HttpResponse('blah')
        else:
            return HttpResponse('not blah')
    else:
        product = ProductForm()
        return render(request, 'add-product_priv.html', {
            'product': product,
        })