from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployerHomeView.as_view(), name="emp-view"),
]
