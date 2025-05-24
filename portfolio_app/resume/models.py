from django.db import models

# Create your models here.
class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

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

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        verbose_name_plural = 'Experiences'
        ordering = ['-end_date', '-start_date']  # Newest experience first

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('lang', 'Programming Languages'),
        ('fw', 'Frameworks & Libraries'),
        ('db', 'Databases'),
        ('tool', 'Tools & Platforms'),
        ('soft', 'Soft Skills'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lang')
    proficiency = models.IntegerField(default=1)  # 1 to 5 scale

    def __str__(self):
        return f"{self.name}"