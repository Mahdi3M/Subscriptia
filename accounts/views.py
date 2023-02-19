from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import User

# Create your views here.

def log_in(request):
    form_msg = None
    if request.method == "POST":
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        print(uname, pword)

        user = authenticate(username=uname, password=pword)
        
        if user is not None:
            print("Logged in.")
            login(request, user)
            if user.is_customer:
                return HttpResponse("Customer Dashboard") #Product er dashboard
            elif user.is_employee:
                return HttpResponse("Employee Dashboard")
        else:
            print("Wrong input.")
            form_msg = "Username or Password is wrong."
            return render(request, "user_profile/login.html", {'form_msg': form_msg})
    print("logged out")
    logout(request)
    return render(request, "user_profile/login.html", {'form_msg': form_msg})


def register(request):
    form_msg = None
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        email_exist = User.objects.all().filter(email=email).exists()
        if not email_exist:
            try:
                print(username, email, password)
                myuser = User.objects.create_user(username=username, email=email, password=password)
                print(myuser)
                myuser.save()
                return redirect('login')
            except Exception:
                form_msg = "Username already taken."
                return render(request, "user_profile/register.html", {'form_msg': form_msg})
        else:
            form_msg = "Email already taken."
            return render(request, "user_profile/register.html", {'form_msg': form_msg})

    return render(request, "user_profile/register.html", {'form_msg': form_msg})


def log_out(request):
    logout(request)
    return redirect('login')



# def home_page(request):
#     if request.method == "POST":
#         uname = request.POST.get('username')
#         pword = request.POST.get('password')

#         user = authenticate(username=uname, password=pword)

#         if user is not None:
#             login(request, user)
#             return render(request, "home/index.html")
#         else:
#             messages.error(request, "Bad Credentials")
#             return redirect('home_page')
#     return render(request, "home/index.html")


# def register_page(request):
#     if request.method == "POST":
#         firstname = request.POST.get('firstName')
#         lastname = request.POST.get('lastName')
#         email = request.POST.get('email')
#         username = request.POST.get('userName')
#         password = request.POST.get('password')
#         repassword = request.POST.get('repassword')

#         if password == repassword:
#             myuser = User.objects.create_user(username, email, password)
#             myuser.first_name = firstname
#             myuser.last_name = lastname

#             myuser.save()
#             messages.success(request, "Your Account has been successfully created.")
#             redirect('home_page')
#         else:
#             messages.error(request, "Password did not match.")

#     return render(request, "home/register.html")


# def log_out(request):
#     logout(request)
#     return redirect('home_page')