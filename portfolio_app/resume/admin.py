from django.contrib import admin
from resume.models import Experience, Education, Skill, RelevantCourse, Language, ProjectSection, ContactInfo, Summary

# Register your models here.
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(RelevantCourse)
admin.site.register(Language)
admin.site.register(ProjectSection)
admin.site.register(ContactInfo)
admin.site.register(Summary)