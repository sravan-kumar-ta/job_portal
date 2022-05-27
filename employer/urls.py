from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployerHomeView.as_view(), name="emp-home"),
    path('add_job', views.AddJobView.as_view(), name="emp-add_job"),
    path('view_jobs', views.ListJobsView.as_view(), name="emp-alljobs"),
    path('jobs/detail/<int:id>/', views.JobDetailView.as_view(), name="emp-jobdetail"),
    path('jobs/change/<int:id>/', views.JobEditView.as_view(), name="emp-jobedit"),
    path('jobs/remove/<int:id>/', views.JobDeleteView.as_view(), name="emp-jobdelete"),
    path('users/accounts/signup/', views.SignUpView.as_view(), name='signup')
]
