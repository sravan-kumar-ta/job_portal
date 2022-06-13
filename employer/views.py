from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from employer.forms import JobForm, SignUpForm, LoginForm, CompanyProfileForm, PasswordResetForm
from employer.models import Job, CompanyProfile, User


# Create your views here.
class EmployerHomeView(TemplateView):
    template_name = "employer/dashboard.html"


class AddJobView(CreateView):
    model = Job
    form_class = JobForm
    template_name = "employer/job-add.html"
    success_url = reverse_lazy("employer:all-jobs")
    error_message = "unknown error"

    def form_valid(self, form):
        form.instance.company = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


class ListJobsView(ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = "employer/job-manage.html"

    def get_queryset(self):
        return Job.objects.filter(company=self.request.user).order_by("-id")


class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = "employer/job-view.html"
    pk_url_kwarg = 'id'


class JobEditView(UpdateView):
    model = Job
    form_class = JobForm
    template_name = "employer/job-update.html"
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy('employer:job-detail', kwargs={'id': self.object.id})


class JobDeleteView(DeleteView):
    model = Job
    pk_url_kwarg = 'id'
    template_name = 'employer/job-delete.html'
    success_url = reverse_lazy('employer:all-jobs')


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('employer:sign-in')

    def form_invalid(self, form):
        messages.error(self.request, "Invalid registration")
        return super().form_invalid(form)


class LogInView(FormView):
    form_class = LoginForm
    template_name = "auth/login.html"

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.role == "employer":
                    return redirect('employer:home')
                elif request.user.role == "candidate":
                    return redirect("cand-home")
            else:
                messages.error(request, "Invalid credentials...")
                return render(request, 'auth/login.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('employer:sign-in')


class ChangePasswordView(TemplateView):
    template_name = "auth/password-reset-request.html"

    def post(self, request, *args, **kwargs):
        password = request.POST.get("password")
        username = request.user
        user = authenticate(request, username=username, password=password)
        if user:
            return redirect("employer:password-reset")
        else:
            messages.error(request, "Wrong password! Please try again...")
            return render(request, self.template_name)


class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = "auth/password-reset.html"
    success_url = reverse_lazy("employer:sign-out")

    def form_valid(self, form):
        new_password = form.cleaned_data.get("password1")
        user = User.objects.get(username=self.request.user)
        user.set_password(new_password)
        user.save()
        return super().form_valid(form)


class CompanyProfileView(CreateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    template_name = "employer/profile-add.html"
    success_url = reverse_lazy("emp-home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EmpViewProfileView(TemplateView):
    template_name = "employer/profile.html"


class EmpProfileEditVIew(UpdateView):
    model = CompanyProfile
    form_class = CompanyProfileForm
    pk_url_kwarg = 'id'
    template_name = "employer/profile-update.html"
    success_url = reverse_lazy("employer:profile-view")
