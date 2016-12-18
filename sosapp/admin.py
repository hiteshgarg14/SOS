from django.contrib import admin

# Register your models here.
from .models import NonUserContactModel, ReportOnceModel, IExperienceModel

admin.site.register(NonUserContactModel)
admin.site.register(ReportOnceModel)
admin.site.register(IExperienceModel)