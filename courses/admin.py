# Register your models here.
from django.contrib import admin
from .models import Course, CourseCategory

admin.site.register(Course)
admin.site.register(CourseCategory)