from django.urls import path
from . import views

urlpatterns = [
    path('', views.cardview, name="cardview"),
    path('<int:product_id>/details/', views.product_single, name="product_single"),
    path('add', views.add_product, name="add_product"),
    path('invoice/',views.invoice, name="invoice"),
    path('about_us/',views.about_us, name="about_us"),
    path('add_to_cart/<id>',views.add_to_cart, name="cart"),
    path('wishlist/<id>',views.wishlist, name="wishlist"),
    path('wish_list/<id>',views.r_wishlist, name="r_wishlist"),
]