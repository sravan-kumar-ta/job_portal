from django import forms
from .models import Job
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
