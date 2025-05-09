from django.db import models
from django.utils import timezone
import ast


# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    skills = models.ManyToManyField(Skill)
    category = models.CharField(max_length=100)
    overview = models.TextField()
    technical_details = models.TextField()
    key_features = models.TextField()
    gallery = models.ImageField(upload_to='project_gallery/', null=True, blank=True)
    chalenges_solution = models.TextField()
    results_impact = models.TextField()
    completed_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title