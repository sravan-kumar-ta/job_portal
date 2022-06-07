from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=120)
    company = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=120)
    salary = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    last_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title


class CompanyProfile(models.Model):
    company_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employer")
    logo = models.ImageField(upload_to="company_profile", null=True)
    location = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
