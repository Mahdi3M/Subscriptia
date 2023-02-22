from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect, HttpResponse
from django.urls import reverse
from .models import *
from django.db.models import Q

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
    user = request.user
    subtotal = float(0)
    cp = CartProduct(user=user,product=product)
    try:
        cp.save()

    except Exception:
        cart = CartProduct.objects.filter(user=user)
        print(cart)
        for c in cart:
            print(c.product.price)
            subtotal += float(c.product.price)
        subtotal = int(subtotal)
        context = {
            'cart': cart,
            'subtotal': subtotal,
        }
        return render(request, 'add_to_cart.html', context)
    #
    cart = CartProduct.objects.filter(user=user)
    for c in cart:
        subtotal += float(c.product.price)
    subtotal = int(subtotal)
    context = {
        'cart': cart,
        'subtotal': subtotal,
    }
    return render(request, 'add_to_cart.html',context)


def r_add_to_cart(request,id):
    product = Product.objects.get(id=id)
    user = request.user
    cart = CartProduct.objects.filter(Q(product=product) & Q(user=user))
    cart.delete()
    cart=CartProduct.objects.filter(user=user)
    subtotal = float(0)
    for c in cart:
        subtotal += float(c.product.price)
    subtotal = int(subtotal)
    context = {
        'cart': cart,
        'subtotal': subtotal,
    }
    return render(request, 'add_to_cart.html',context)
    
def invoice(request):
    user = request.user
    cart = CartProduct.objects.all().filter(user=user)
    status = "pending"
    subtotal = float(0)
    for c in cart:
        product=c.product
        order=Order(user=user,product=product,status=status)
        try:
            order.save()
        except Exception as e:
            break

    cart = CartProduct.objects.all().filter(user=user)

    cart = CartProduct.objects.all().filter(user=user)
    cart.delete()
    # print(cart)
    subtotal=int(subtotal)
    order = Order.objects.filter(user=user)
    r= random.randint(0,100000)
    for o in order:
        subtotal += float(o.product.price)
        print(subtotal)
    context = {
        'order': order,
        'subtotal': subtotal,
        'r' : r,
    }
    return render(request,'invoice.html',context)

def r_wishlist(request,id):
    user = request.user
    product = Product.objects.get(id=id)
    wish_list = Wishlist_Product.objects.filter(Q(product=product) & Q(user=user))
    wish_list.delete()
    wish_list = Wishlist_Product.objects.filter(user=user)
    context = {
        'wish_list': wish_list,
    }
    return render(request, 'wishlist.html',context)
def wishlist(request,id):
    product = Product.objects.get(id=id)
    user = request.user
    wish = Wishlist_Product(user=user, product=product)
    try:
        wish.save()
    except Exception as e:
        wish_list = Wishlist_Product.objects.filter(user=user)
        # for c in cart:
        #     print(c.product.name)
        context = {
            'wish_list': wish_list,
        }
        return render(request,'wishlist.html',context)

    wish_list = Wishlist_Product.objects.filter(user=user)
    context = {
        'wish_list': wish_list,
    }
    return render(request,'wishlist.html',context)




