from django import forms
from django.utils.translation import gettext as _

from .models import Job, CompanyProfile
from django.contrib.auth.forms import UserCreationForm
from employer.models import User


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('company', 'created_date')
        widgets = {
            'job_title': forms.TextInput(attrs={
                "class": "form-control form-control-user",
                "placeholder": "Enter job title..",
            }),
            'location': forms.TextInput(attrs={
                "class": "form-control form-control-user",
                "placeholder": "Location..",
            }),
            'salary': forms.NumberInput(attrs={
                "class": "form-control form-control-user",
                "placeholder": "Salary..",
            }),
            'experience': forms.NumberInput(attrs={
                "class": "form-control form-control-user",
                "placeholder": "How many years of experience..",
            }),
            'last_date': forms.DateInput(attrs={
                'class': "form-control form-control-user",
                "type": "date"
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': "form-control form-control-user",
            })
        }


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Password",
        "id": "password1"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Confirm Password",
        "id": "password2"
    }))

    role = forms.ChoiceField(choices=User.options, widget=forms.Select(attrs={
        "class": "form-control",
    }), )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'role', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }),
            'last_name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Last Name",
            }),
            'username': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Username",
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Email",
            }),
            'phone': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Phone",
            }),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control form-control-user",
        "placeholder": "Enter username...",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control form-control-user",
        "placeholder": "Enter Password...",
    }))


class PasswordResetForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "enter password"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "confirm password"
    }))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Password mismatch! Try again..."), code="password_mismatch")
        return cleaned_data


class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        exclude = ("user",)

        widgets = {
            'company_name': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "First Name",
            }),
            'location': forms.TextInput(attrs={
                "class": "form-control",
            }),
            'services': forms.TextInput(attrs={
                "class": "form-control",
            }),
            'description': forms.TextInput(attrs={
                "class": "form-control",
            }),
        }
