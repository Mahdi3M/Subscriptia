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
    if request.method == "POST":
        rating = request.POST.get('review-rating')
        comment = request.POST.get('review')
        r = Review.objects.get(user=request.user, product=product)
        r.rating = rating
        r.save()
        if comment is not (None or ""):
            rc = ReviewComment(review=r, comment=comment)
            rc.save()

    try:
        review = Review.objects.get(user=request.user, product=product)
    except Exception:
        r = Review(user=request.user, product=product)
        r.save()
        review = r

    reviewAll = Review.objects.all().filter(product=product)
    reviewComment = ReviewComment.objects.all().filter(review__in=reviewAll)

    ratingTotal = 0
    for r in reviewAll:
        if r.rating:
            ratingTotal = ratingTotal + r.rating

    print(ratingTotal, len(reviewAll))

    return render(request, 'product_single.html', {
        'product': product,
        'products': products,
        'stars': [None] * product.rating,
        'new_price': product.price - (product.price * product.discount / 100),
        'review': review,
        'review_comments': reviewComment,
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

def add_to_cart(request,id):
    product = Product.objects.get(id=id)
    price = product.price
    user = request.user
    cp = CartProduct(user=user,product=product,subtotal=price)
    try:
        cp.save()
    except Exception as e:
        cart = CartProduct.objects.filter(user=user)
        # for c in cart:
        #     print(c.product.name)
        context = {
            'cart': cart,
        }
        print(e)
        return render(request, 'add_to_cart.html', context)

    cart = CartProduct.objects.filter(user=user)
    # for c in cart:
    #     print(c.product.name)
    context = {
        'cart': cart,
    }
    return render(request, 'add_to_cart.html',context)

def invoice(request):
    return render(request,'invoice.html')