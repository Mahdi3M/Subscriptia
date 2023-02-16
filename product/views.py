from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
<<<<<<< Updated upstream
    return render(request,'base.html')

def product_single(request, product_id):
    return render(request, 'product_single.html', {})
>>>>>>> Stashed changes
