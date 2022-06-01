from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployerHomeView.as_view(), name="emp-home"),
    path('add_job', views.AddJobView.as_view(), name="emp-add_job"),
    path('view_jobs', views.ListJobsView.as_view(), name="emp-alljobs"),
    path('jobs/detail/<int:id>/', views.JobDetailView.as_view(), name="emp-jobdetail"),
    path('jobs/change/<int:id>/', views.JobEditView.as_view(), name="emp-jobedit"),
    path('jobs/remove/<int:id>/', views.JobDeleteView.as_view(), name="emp-jobdelete"),
    path('users/accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('users/account/signin/', views.LogInView.as_view(), name="signin"),
    path('users/account/signout/', views.signout_view, name="signout"),
    path('users/password/change/', views.ChangePasswordView.as_view(), name="password-change"),
    path('users/password/reset/', views.PasswordResetView.as_view(), name="password-reset")
]
