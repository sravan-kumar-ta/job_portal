from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployerHomeView.as_view(), name="emp-home"),
    path('add_job', views.AddJobView.as_view(), name="emp-add_job"),
    path('view_jobs', views.ListJobsView.as_view(), name="emp-alljobs"),
    path('jobs/detail/<int:id>/', views.JobDetailView.as_view(), name="emp-jobdetail")
]
