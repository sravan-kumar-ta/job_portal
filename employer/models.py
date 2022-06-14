from django.db import models
from django.contrib.auth.models import User, AbstractUser


# Create your models here.
class User(AbstractUser):
    options = (
        ("employer", 'employer'),
        ("candidate", "candidate")
    )
    role = models.CharField(max_length=120, choices=options, default="candidate")
    phone = models.CharField(max_length=120, null=True)


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


class Applications(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applicant")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    options = (
        ("applied", "applied"),
        ("accepted", "accepted"),
        ("rejected", "rejected"),
        ("pending", "pending"),
        ("cancelled", "cancelled"),
    )
    status = models.CharField(choices=options, default="applied", max_length=120)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("applicant", 'job')
