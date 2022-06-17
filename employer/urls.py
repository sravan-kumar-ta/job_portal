from django.urls import path
from employer import views

app_name = "employer"

urlpatterns = [
    path('', views.home),
    path('home', views.EmployerHomeView.as_view(), name="home"),
    path('add_job/', views.AddJobView.as_view(), name="add-job"),
    path('view_jobs/', views.ListJobsView.as_view(), name="all-jobs"),
    path('job/<int:id>/', views.JobDetailView.as_view(), name="job-detail"),
    path('job/<int:id>/update/', views.JobEditView.as_view(), name="job-update"),
    path('job/<int:id>/delete/', views.JobDeleteView.as_view(), name="job-delete"),

    path('accounts/signup/', views.SignUpView.as_view(), name='sign-up'),
    path('accounts/sign_in/', views.LogInView.as_view(), name="sign-in"),
    path('accounts/sign_out/', views.signout_view, name="sign-out"),
    path('password_change/', views.ChangePasswordView.as_view(), name="password-reset-request"),
    path('password_reset/', views.PasswordResetView.as_view(), name="password-reset"),

    path('profile/', views.EmpViewProfileView.as_view(), name="profile-view"),
    path('profile/add/', views.CompanyProfileView.as_view(), name='profile-add'),
    path('profile/<int:id>/update/', views.EmpProfileEditVIew.as_view(), name="profile-update")
]
