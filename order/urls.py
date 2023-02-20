from django.urls import path
from .views import *

urlpatterns = [
    path('', order, name="order"),
    path('add_to_cart/<id>',add_to_cart, name="cart"),
]