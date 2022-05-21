from django import forms


class JobForm(forms.Form):
    job_title = forms.CharField()
    company = forms.CharField()
    location = forms.CharField()
    salary = forms.IntegerField()
    experience = forms.IntegerField()
