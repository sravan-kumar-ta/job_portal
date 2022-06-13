from django.contrib import admin
from .models import Job, User, CompanyProfile, Applications

# Register your models here.
admin.site.register(Job)
admin.site.register(User)
admin.site.register(CompanyProfile)
admin.site.register(Applications)
