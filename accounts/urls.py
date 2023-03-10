from django.urls import path
from accounts import views

app_name = "account"

urlpatterns = [
    path('', views.profile, name="profile"),
    path('login/', views.log_in, name="login"),
    path('register/', views.register, name="register"),
    path('logout', views.log_out, name="logout"),
]