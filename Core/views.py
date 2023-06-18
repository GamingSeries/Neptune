from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import UserProfile
# from .forms import UserProfileForm, LoginForm
# from django.contrib.auth import login as auth_login
# Create your views here.

def home(request):

    return render(request,  "core/home.html")

def cart(request):
    return render(request, "core/cart.html")

def settings(request):
    return render(request, "core/settings.html")

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        form.request = request
        if form.is_valid():
            print("Form is valid")
            auth_login(request, form.user_cache)
            print("User is authenticated")
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, "core/login.html", {'form': form})

#all the categories (men,women,kids) will be displayed here

def for_men(request):
    
    return render(request, "core/categories/for_men.html")

def for_kids(request):

    return render(request, "core/categories/for_kids.html")

def for_women(request):

    return render(request, "core/categories/for_women.html")