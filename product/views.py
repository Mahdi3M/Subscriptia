from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.urls import reverse
from .models import *

# Create your views here.


def index(request):
    return render(request, 'home.html')


def product_single(request, product_id):
    product = Product.objects.get(id=product_id)
    products = list(Product.objects.filter(name=product.name))
    quantity = 1 
    return render(request, 'product_single.html', {
        'product': product,
        'products': products,
        'stars': [None] * product.rating,
        'new_price': product.price - (product.price * product.discount / 100),
    })
    # return HttpResponse(f'The product is {Product.objects.get(id=product_id).name}')


def add_product(request):
    product = Product()
    if request.method == 'POST':
        product.name = request.POST['product_name']
        product.description = request.POST['product_desc']
        product.category = request.POST['product_category']
        product.plan_name = request.POST['product_plan_name']
        product.price = request.POST['product_price']
        product.discount = request.POST['product_discount']
        product.slug = f"{product.name}_{product.plan_name}".replace(" ", "")
        if request.FILES.get('product_image'):
            image_file = request.FILES.get('product_image')
            product.image = image_file
        product.save()
        return HttpResponsePermanentRedirect(reverse('product_single', args=(product.id,)))
    product = Product()
    categories = list()
    for c in range(0, len(Product.category.field.choices)):
        categories.append(Product.category.field.choices[c][1])
    return render(request, 'add-product_priv.html', {
            'product': product,
            'categories' : categories,
        })