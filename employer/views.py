from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from employer.forms import JobForm
from employer.models import Job


# Create your views here.
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class AddJobView(View):
    def get(self, request):
        form = JobForm()
        return render(request, "emp-add_job.html", {"form": form})

    def post(self, request):
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "emp-home.html")
        else:
            return render(request, "emp-add_job.html", {"form": form})


class ListJobsView(View):
    def get(self, request):
        jobs = Job.objects.all()
        return render(request, 'emp-list_jobs.html', {'jobs': jobs})


class JobDetailView(View):
    def get(self, request, id):
        job = Job.objects.get(id=id)
        return render(request, 'emp-detail_job.html', {'job': job})