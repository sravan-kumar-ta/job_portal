from django.db import models
from employer.models import User


# Create your models here.
class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="candidate")
    profile_pic = models.ImageField(upload_to="cand_profiles")
    resume = models.FileField(upload_to="cvs", null=True)
    qualification = models.CharField(max_length=120)
    skills = models.CharField(max_length=120)
    experience = models.PositiveIntegerField(default=0)
