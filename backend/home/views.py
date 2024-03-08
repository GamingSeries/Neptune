from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, './html/index.html')

def login(request):
    #create login handler
    
    return render(request, './html/login.html')
