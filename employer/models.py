from django.db import models


# Create your models here.
class Job(models.Model):
    job_title = models.CharField(max_length=120)
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    salary = models.PositiveIntegerField(null=True)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.job_title
