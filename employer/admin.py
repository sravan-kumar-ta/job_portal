from django.contrib import admin
from .models import Job, User, CompanyProfile

# Register your models here.
admin.site.register(Job)
admin.site.register(User)
admin.site.register(CompanyProfile)
