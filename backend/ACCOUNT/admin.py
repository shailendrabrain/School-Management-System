from django.contrib import admin
from .models import StudentProfile, TeacherProfile


@admin.register(StudentProfile)
class StudentProfile(admin.ModelAdmin):
    list_display = ('user', 'name', 'enrollment', 'standard')


@admin.register(TeacherProfile)
class TeacherProfile(admin.ModelAdmin):
    list_display=['user','name']
