from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView, FormView

from employer.decorators import signin_required
from employer.forms import JobForm, SignUpForm, LoginForm, CompanyProfileForm, PasswordResetForm
from employer.models import Jobs, CompanyProfiles, CustomUser, Applications


# Create your views here.
@signin_required
def home(request):
    if request.user.role == "employer":
        return redirect("employer:home")
    else:
        return redirect("candidate:home")


class EmployerHomeView(TemplateView):
    template_name = "employer/dashboard.html"


@method_decorator(signin_required, name='dispatch')
class AddJobView(CreateView, SuccessMessageMixin):
    model = Jobs
    form_class = JobForm
    template_name = "employer/job-add.html"
    success_url = reverse_lazy("employer:all-jobs")
    error_message = "Invalid form request"
    success_message = "Job added successfully.."

    def form_valid(self, form):
        form.instance.company = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)


@method_decorator(signin_required, name='dispatch')
class ListJobsView(ListView):
    model = Jobs
    context_object_name = 'jobs'
    template_name = "employer/job-manage.html"

    def get_queryset(self):
        return Jobs.objects.filter(company=self.request.user).order_by("-id")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)


@method_decorator(signin_required, name='dispatch')
class JobDetailView(DetailView):
    model = Jobs
    context_object_name = 'job'
    template_name = "employer/job-view.html"
    pk_url_kwarg = 'id'


@method_decorator(signin_required, name='dispatch')
class JobEditView(UpdateView):
    model = Jobs
    form_class = JobForm
    template_name = "employer/job-update.html"
    pk_url_kwarg = 'id'

    def get_success_url(self):
        messages.success(self.request, "Job updated..")
        return reverse_lazy('employer:job-detail', kwargs={'id': self.object.id})


@method_decorator(signin_required, name='dispatch')
class JobDeleteView(DeleteView, SuccessMessageMixin):
    model = Jobs
    pk_url_kwarg = 'id'
    template_name = 'employer/job-delete.html'
    success_message = "Job deleted"
    success_url = reverse_lazy('employer:all-jobs')

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return super().get_success_url()


class SignUpView(CreateView):
    model = CustomUser
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
                    return redirect("employer:home")
                elif request.user.role == "candidate":
                    return redirect("candidate:home")
            else:
                messages.error(request, "Invalid credentials...")
                return render(request, 'auth/login.html', {'form': form})


def signout_view(request):
    logout(request)
    return redirect('employer:sign-in')


@method_decorator(signin_required, name='dispatch')
class ChangePasswordView(TemplateView):
    template_name = "auth/password-reset-request.html"

    def post(self, request):
        password = request.POST.get("password")
        username = request.user
        user = authenticate(request, username=username, password=password)
        if user:
            return redirect("employer:password-reset")
        else:
            messages.error(request, "Wrong password! Please try again...")
            return render(request, self.template_name)


@method_decorator(signin_required, name='dispatch')
class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = "auth/password-reset.html"
    success_url = reverse_lazy("employer:sign-out")

    def form_valid(self, form):
        new_password = form.cleaned_data.get("password1")
        user = CustomUser.objects.get(username=self.request.user)
        user.set_password(new_password)
        user.save()
        return super().form_valid(form)


@method_decorator(signin_required, name='dispatch')
class CompanyProfileView(CreateView):
    model = CompanyProfiles
    form_class = CompanyProfileForm
    template_name = "employer/profile-add.html"
    success_url = reverse_lazy("employer:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(signin_required, name='dispatch')
class EmpViewProfileView(TemplateView):
    template_name = "employer/profile.html"


@method_decorator(signin_required, name='dispatch')
class EmpProfileEditVIew(UpdateView):
    model = CompanyProfiles
    form_class = CompanyProfileForm
    pk_url_kwarg = 'id'
    template_name = "employer/profile-update.html"
    success_url = reverse_lazy("employer:profile-view")


@method_decorator(signin_required, name='dispatch')
class ApplicationListView(ListView):
    model = Applications
    context_object_name = "applications"
    template_name = "employer/job-applications.html"

    def get_queryset(self):
        job_id = self.kwargs.get("job_id")
        return Applications.objects.filter(job=job_id).exclude(status="Cancelled")


@method_decorator(signin_required, name='dispatch')
class ApplicationDetailView(DetailView):
    model = Applications
    pk_url_kwarg = "app_id"
    context_object_name = "application"
    template_name = "employer/application.html"


@signin_required
def reject_application(request, app_id):
    application = Applications.objects.get(id=app_id)
    application.status = "Rejected"
    application.save()
    return redirect("employer:application-list", app_id)


def accept_application(request, app_id):
    application = Applications.objects.get(id=app_id)
    application.status = 'Accepted'
    application.save()
    mail_id = application.applicant.candidate.email
    if mail_id:
        message = request.POST.get('message')
        send_mail(
            'Your application accepted',
            message,
            'Job Portal <srawz101@gmail.com.com>',
            [mail_id],
            fail_silently=False,
        )
    return redirect("employer:application-list", application.job.id)
