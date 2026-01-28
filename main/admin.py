from django.contrib import admin
from . models import studs, assessments,courses
# Register your models here.
admin.site.register(studs)
admin.site.register(courses)
admin.site.register(assessments)