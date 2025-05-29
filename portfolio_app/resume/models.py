from django.db import models
from projects.models import Project

# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f"{self.degree} from {self.institution}"

    class Meta:
        verbose_name_plural = 'Educations'
        ordering = ['-end_date', '-start_date']  # Newest education first

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution} ({self.start_date} - {self.end_date if self.end_date else 'Present'})"

class Experience(models.Model):
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    skills_used = models.ManyToManyField('Skill', blank=True, related_name='experiences', limit_choices_to={'category': 'tech'})

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        verbose_name_plural = 'Experiences'
        ordering = ['-end_date', '-start_date']  # Newest experience first

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technical Skills'),
        ('soft', 'Soft Skills'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lang')


    def __str__(self):
        return f"{self.name}"

class RelevantCourse(models.Model):
    education = models.ForeignKey(Education, on_delete=models.CASCADE, related_name='relevant_courses')
    course_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.course_name} ({self.education.institution})"

    class Meta:
        verbose_name_plural = 'Relevant Courses'
        ordering = ['course_name']

class Language(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.proficiency})"

    class Meta:
        verbose_name_plural = 'Languages'
        ordering = ['name']

class Summary(models.Model):
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Resume Summary"

    class Meta:
        verbose_name_plural = 'Summaries'
        verbose_name = 'Summary'
        ordering = ['id']  # Ensures a single instance is always returned

class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)


class ProjectSection(models.Model):
    projects = models.ManyToManyField(Project, related_name='resume_sections')
    title = models.CharField(max_length=255, default="Projects")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Project Sections'

