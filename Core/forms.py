from django import forms
from .models import UserProfile
from django.contrib.auth import authenticate

class UserProfileForm(forms.ModelForm):
    class Meta :
        model = UserProfile
        fields = '__all__'
        
class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email/password")
        return cleaned_data
    