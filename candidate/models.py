from django.db import models
from employer.models import CustomUser


# Create your models here.
class CandidateProfiles(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="candidate")
    profile_pic = models.ImageField(upload_to="files/profile_pic")
    resume = models.FileField(upload_to="files/resumes_or_cvs", null=True)
    qualification = models.CharField(max_length=120)
    skills = models.CharField(max_length=120)
    experience = models.PositiveIntegerField(default=0)
