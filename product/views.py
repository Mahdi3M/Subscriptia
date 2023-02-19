from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'home.html')


def product_single(request, product_id):
    return render(request, 'product_single.html', {})

