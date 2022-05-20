from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"
