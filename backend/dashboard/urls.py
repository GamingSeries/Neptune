from django.urls import path, include
from .views import DashboardView

urlpatterns = [
    path('dashboard/<str:user_type>/', DashboardView.as_view(), name='dashboard'),
]