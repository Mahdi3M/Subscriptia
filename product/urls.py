from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:product_id>/details/', views.product_single, name="product_single"),
    path('add', views.add_product, name="add_product"),
    path('invoice/',views.invoice, name="invoice"),
    path('add_to_cart/<id>',views.add_to_cart, name="cart"),
]