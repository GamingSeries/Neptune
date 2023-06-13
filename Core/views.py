from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile
# Create your views here.

def home(request):
    context = {}
    context['userprofile'] = UserProfile.objects.all()
    return render(request,  "core/home.html", context)

def cart(request):
    return render(request, "core/cart.html")

def settings(request):
    return render(request, "core/settings.html")