from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from employer.forms import JobForm, SignUpForm, LoginForm
from employer.models import Job


# Create your views here.
class EmployerHomeView(TemplateView):
    template_name = "emp-home.html"


class AddJobView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "emp-add_job.html"
    success_url = reverse_lazy("emp-alljobs")
    # def get(self, request):
    #     form = JobForm()
    #     return render(request, "emp-add_job.html", {"form": form})
    #
    # def post(self, request):
    #     form = JobForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('emp-alljobs')
    #     else:
    #         return render(request, "emp-add_job.html", {"form": form})


class ListJobsView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'emp-list_jobs.html'
    # def get(self, request):
    #     jobs = Job.objects.all()
    #     return render(request, 'emp-list_jobs.html', {'jobs': jobs})


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'emp-detail_job.html'
    pk_url_kwarg = 'id'
    # def get(self, request, id):
    #     job = Job.objects.get(id=id)
    #     return render(request, 'emp-detail_job.html', {'job': job})


class JobEditView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = 'emp-editjob.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('emp-alljobs')

    # def get(self, request, id):
    #     job = Job.objects.get(id=id)
    #     form = JobForm(instance=job)
    #     return render(request, 'emp-editjob.html', {'form': form})
    #
    # def post(self, request, id):
    #     job = Job.objects.get(id=id)
    #     form = JobForm(request.POST, instance=job)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('emp-alljobs')
    #     else:
    #         return render(request, 'emp-editjob.html', {'form': form})


class JobDeleteView(DeleteView):
    model = Job
    template_name = 'emp-jobdelete.html'
    success_url = reverse_lazy('emp-alljobs')
    pk_url_kwarg = 'id'
    # def get(self, request, id):
    #     job = Job.objects.get(id=id)
    #     job.delete()
    #     return redirect('emp-alljobs')


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'user_signup.html'
    success_url = reverse_lazy('emp-alljobs')


class LogInView(FormView):
    form_class = LoginForm
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('emp-alljobs')
            else:
                return render(request, 'login.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('signin')
