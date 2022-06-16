from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    options = (
        ("employer", 'Employer'),
        ("candidate", "Candidate")
    )
    role = models.CharField(max_length=120, choices=options, default="candidate")
    phone = models.CharField(max_length=120, null=True)


class Jobs(models.Model):
    job_title = models.CharField(max_length=120)
    company = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=120)
    salary = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(default=0)
    created_date = models.DateField(auto_now_add=True)
    last_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.job_title


class CompanyProfiles(models.Model):
    company_name = models.CharField(max_length=100)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="employer")
    logo = models.ImageField(upload_to="files/company_logo", null=True)
    location = models.CharField(max_length=100)
    services = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Applications(models.Model):
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applicant')
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    options = (
        ("applied", "Applied"),
        ("accepted", "Accepted"),
        ("rejected", "Rejected"),
        ("pending", "Pending"),
        ("cancelled", "Cancelled")
    )
    status = models.CharField(choices=options, max_length=120, default="applied")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("applicant", "job")
