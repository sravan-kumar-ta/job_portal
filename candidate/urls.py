from django.urls import path
from candidate import views

app_name = "candidate"

urlpatterns = [
    path('home/', views.CandidateHomeView.as_view(), name="home"),
    path('profile/add/', views.CandidateProfileView.as_view(), name="add-profile"),
    path('profile/detail/', views.CandidateProfileDetailView.as_view(), name="view-profile"),
    path('profile/update/', views.CandidateProfileEditView.as_view(), name="update-profile"),

    path('jobs/all/', views.CandidateJobListView.as_view(), name="jobs-list"),
    path('jobs/details/<int:id>/', views.CandidateJobDetailView.as_view(), name="job-view"),
    path('jobs/apply_now/<int:id>/', views.apply_now, name="apply-now"),

    path('applications/all/', views.ApplicationListView.as_view(), name="applications"),
    path('application/cancellation/<int:id>/', views.application_cancellation, name="cancel-application")
]
