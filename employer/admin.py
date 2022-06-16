from django.contrib import admin
from .models import Jobs, CustomUser, CompanyProfiles, Applications

# Register your models here.
admin.site.register(Jobs)
admin.site.register(CustomUser)
admin.site.register(CompanyProfiles)
admin.site.register(Applications)
