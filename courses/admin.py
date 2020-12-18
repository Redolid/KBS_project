from django.contrib import admin
from .models import courses,student

# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ['GPA', 'Term', "student_level"]
@admin.register(courses)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['Course_name', 'Course_code', 'semester', 'Taken', 'level']
