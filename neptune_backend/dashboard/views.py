from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class DashboardView(APIView):
    
    def get(self, request, *args, **kwargs):
        user_type = kwargs.get('user_type')

        if user_type == 'admin':
            return self.admin_dashboard(request)
        elif user_type == 'staff':
            return self.staff_dashboard(request)
        elif user_type == 'seller':
            return self.seller_dashboard(request)
        else:
            return self.user_dashboard(request)

    def user(self, request):
        data = {"message": "User Dashboard"}
        return Response(data)

    def admin(self, request):
        data = {"message": "Admin Dashboard"}
        return Response(data)

    def staff(self, request):
        data = {"message": "Staff Dashboard"}
        return Response(data)

    def seller(self, request):
        data = {"message": "Seller Dashboard"}
        return Response(data)