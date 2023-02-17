from django.urls import path
from home import views

urlpatterns = [
    path('login/', views.home_page, name="home_page"),
]