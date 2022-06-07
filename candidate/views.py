from django.shortcuts import render
from django.views.generic import TemplateView


class CandidateHomeView(TemplateView):
    template_name = "can-home.html"
