# Create your models here.
from django.db import models

    
class CourseCategory(models.Model):
    course_category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.course_category


class Course(models.Model):

    LEVELS = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advance'),
    ]

    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    estimated_price = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='courses/')
    overview = models.CharField(max_length=200, null=True, blank=True)
    key_topics = models.CharField(max_length=200, null=True, blank=True)
    outcome = models.CharField(max_length=200, null=True, blank=True)
    whatsapp = models.URLField()
    duration = models.CharField(max_length=255, null=True, blank=True)
    level = models.CharField(max_length=255, choices=LEVELS, default='I')

    def __str__(self):
        return self.title