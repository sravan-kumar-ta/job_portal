from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, ListView, DetailView
from candidate.forms import CandidateProfileForm, CandidateProfileUpdateForm
from candidate.models import CandidateProfile
from employer.models import User, Job


class CandidateHomeView(TemplateView):
    template_name = "candidates/can-home.html"


class CandidateProfileView(CreateView):
    model = CandidateProfile
    form_class = CandidateProfileForm
    template_name = "candidates/can-profile.html"
    success_url = reverse_lazy("cand-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CandidateProfileDetailView(TemplateView):
    template_name = "candidates/can-profiledetail.html"


class CandidateProfileEditView(FormView):
    template_name = "candidates/can-editprof.html"
    form_class = CandidateProfileUpdateForm

    def get(self, request, *args, **kwargs):
        prodetails = CandidateProfile.objects.get(user=request.user)
        form = CandidateProfileUpdateForm(instance=prodetails, initial={"first_name": request.user.first_name,
                                                                        "last_name": request.user.last_name,
                                                                        "phone": request.user.phone})
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        prodetails = CandidateProfile.objects.get(user=request.user)
        form = self.form_class(instance=prodetails, data=request.POST, files=request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data.pop("first_name")
            last_name = form.cleaned_data.pop("last_name")
            phone = form.cleaned_data.pop("phone")
            form.save()

            user = User.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            user.phone = phone
            user.save()

            return redirect("cand-home")
        else:
            return render(request, self.template_name, {"form": form})


class CandidateJobListView(ListView):
    model = Job
    context_object_name = "jobs"
    template_name = "candidates/joblist.html"

    def get_queryset(self):
        return self.model.objects.all().order_by("-created_date")


class CandidateJobDetailView(DetailView):
    model = Job
    context_object_name = "job"
    template_name = "candidates/jobdetail.html"
    pk_url_kwarg = "id"
