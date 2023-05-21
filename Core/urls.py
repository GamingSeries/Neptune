from django.urls import path, include
from .views import home, cart

urlpatterns = [
    path("home/", home, name="home"),
    path("cart/", cart, name="cart")
]