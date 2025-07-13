from django.forms import ModelForm, PasswordInput
from django.contrib.auth.hashers import make_password
from .models import *

class RegisterForm(ModelForm):
    class Meta:
        model = Korisnik
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'role', 'status']
        widgets = {
            'password': PasswordInput(),
        }

    def save(self, commit=True): 
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user