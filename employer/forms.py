from django import forms
from .models import Job, CompanyProfile
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from employer.models import User


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'created_date', 'is_active')
        widgets = {
            'last_date': forms.DateInput(attrs={'class': "form-control", "type": "date"})
        }

    # def clean(self):
    #     cleaned_data = super().clean()
    #     l_date = cleaned_data.get("last_date")
    #
    #

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'role', 'phone']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()
        pwd1 = cleaned_data.get("password1")
        pwd2 = cleaned_data.get("confirm_password")

        if pwd1 != pwd2:
            msg = "Password mismatch"
            self.add_error("password1", msg)


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ("user",)
