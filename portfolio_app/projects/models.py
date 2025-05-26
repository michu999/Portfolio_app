from django.db import models
# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='technology_icons/', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['name']

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']