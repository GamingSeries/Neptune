from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('home/', views.home, name='home'),
]