from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
# Create your views here.


def home(request):
    return render(request, './html/index.html')

def login(request):
    return render(request, './html/login.html')


#registering user 
def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})