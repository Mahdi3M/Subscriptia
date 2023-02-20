from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:product_id>/details/', views.product_single, name="product_single"),
    path('add', views.add_product, name="add_product" )

]