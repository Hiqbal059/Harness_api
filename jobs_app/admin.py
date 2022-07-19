from django.contrib import admin
from jobs_app.models import Job, Skill
# Register your models here.

admin.site.register(Job, Skill)
