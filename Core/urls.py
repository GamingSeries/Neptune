from django.urls import path, include
from .views import home, cart,settings

urlpatterns = [
    path("home/", home, name="home"),
    path("cart/", cart, name="cart"),
    path("settings/", settings, name="settings"),
]