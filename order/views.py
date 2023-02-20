from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from django.db import IntegrityError
import requests

# Create your views here.

def product(request):
    return render(request,'order/product_list.html')

def order(request):
    product = Product.objects.all()
    # for p in product:
    #     print(p.id)
    context = {
        'product' : product,
    }
    return render(request,'order/home.html',context)

def add_to_cart(request,id):
    product=Product.objects.get(id=id)
    price=product.price
    cp=CartProduct(product=product,subtotal=price)
    try:
        cp.save()
    except Exception:
        return render(request, 'order/add_to_cart.html')

    cart = CartProduct.objects.all()
    # for c in cart:
    #     print(c.product.name)
    context = {
        'cart': cart,
    }
    return render(request, 'order/add_to_cart.html',context)
