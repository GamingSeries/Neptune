from django.urls import path, include
from .views import home, cart,settings,for_men,for_kids,for_women,login

urlpatterns = [
    path("home/", home, name="home"),
    path("cart/", cart, name="cart"),
    path("settings/", settings, name="settings"),
    path("for-men/",for_men, name="for_men"),
    path("for-kids/",for_kids, name="for_kids"),
    path("for-women/", for_women, name="for_women"),
    path("login/", login, name="login"),
] 