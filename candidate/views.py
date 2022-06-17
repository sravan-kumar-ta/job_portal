from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, ListView, DetailView
from candidate.forms import CandidateProfileForm, CandidateProfileUpdateForm
from candidate.models import CandidateProfiles
from employer.models import CustomUser, Jobs, Applications


class CandidateHomeView(TemplateView):
    template_name = "candidate/home.html"


class CandidateProfileView(CreateView):
    model = CandidateProfiles
    form_class = CandidateProfileForm
    template_name = "candidate/profile_add.html"
    success_url = reverse_lazy("candidate:view-profile")

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Your profile has been added..!")
        return super().form_valid(form)


class CandidateProfileDetailView(TemplateView):
    template_name = "candidate/profile.html"


class CandidateProfileEditView(FormView):
    template_name = "candidate/profile_add.html"
    form_class = CandidateProfileUpdateForm

    def get(self, request, *args, **kwargs):
        profile_details = CandidateProfiles.objects.get(user=request.user)
        form = CandidateProfileUpdateForm(instance=profile_details, initial={"first_name": request.user.first_name,
                                                                             "last_name": request.user.last_name,
                                                                             "phone": request.user.phone})
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        profile_details = CandidateProfiles.objects.get(user=request.user)
        form = self.form_class(instance=profile_details, data=request.POST, files=request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.pop("first_name")
            last_name = form.cleaned_data.pop("last_name")
            phone = form.cleaned_data.pop("phone")
            form.save()

            user = CustomUser.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.save()
            messages.success(request, "Your profile has been updated..!")
            return redirect("candidate:view-profile")
        else:
            messages.error(request, "Error occurred while updating profile..!")
            return render(request, self.template_name, {"form": form})


class CandidateJobListView(ListView):
    model = Jobs
    context_object_name = "jobs"
    template_name = "candidate/job_list.html"

    def get_queryset(self):
        return self.model.objects.filter(is_active=True).order_by("-created_date")


class CandidateJobDetailView(DetailView):
    model = Jobs
    context_object_name = "job"
    template_name = "candidate/job_details.html"
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        application = None
        try:
            application = Applications.objects.get(applicant=self.request.user, job=self.object)
        except:
            pass
        finally:
            context['application'] = application
        return context


def apply_now(request, *args, **kwargs):
    user = request.user
    job_id = kwargs.get("id")
    job = Jobs.objects.get(id=job_id)
    try:
        application = Applications.objects.get(applicant=user, job=job)
        application.status = "Applied"
        application.save()
    except:
        Applications.objects.create(applicant=user, job=job)
    messages.success(request, "Your applications has been posted successfully..!")
    return redirect("candidate:applications")


class ApplicationListView(ListView):
    model = Applications
    template_name = 'candidate/applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return Applications.objects.filter(applicant=self.request.user)


def application_cancellation(request, *args, **kwargs):
    app_id = kwargs.get("id")
    application = Applications.objects.get(id=app_id)
    application.status = "Cancelled"
    application.save()
    messages.success(request, "Your application cancelled..")
    return redirect("candidate:applications")
