from django.contrib import admin

# Register your models here.
from .models import NonUserContactModel, ReportOnceModel, IExperienceModel, ProfileModel

admin.site.register(NonUserContactModel)
admin.site.register(ReportOnceModel)
admin.site.register(IExperienceModel)
admin.site.register(ProfileModel)
