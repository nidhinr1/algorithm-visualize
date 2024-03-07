from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class signupform(UserCreationForm):
    class meta:
        model=User
        fields=['username','password','password1']
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
