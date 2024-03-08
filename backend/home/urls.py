from django.urls import path
from . import views

urlpatterns = [
    # Add your URL patterns here
    path('neptune/', views.home, name='home'),
    
]