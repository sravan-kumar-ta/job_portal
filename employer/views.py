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
            j_name = form.cleaned_data.get("job_title")
            c_name = form.cleaned_data.get("company")
            location = form.cleaned_data.get("location")
            salary = form.cleaned_data.get("salary")
            exp = form.cleaned_data.get("experience")
            Job.objects.create(
                job_title=j_name,
                company=c_name,
                location=location,
                salary=salary,
                experience=exp
            )
            return render(request, "emp-home.html")
        else:
            return render(request, "emp-add_job.html", {"form": form})
