from django.contrib import admin
from resume.models import Experience, Education, Skill

# Register your models here.
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)