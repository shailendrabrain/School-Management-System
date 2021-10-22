from django.contrib import admin
from .models import Attendance, Subject
# Register your models here.

@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display=['student','date','subject']


@admin.register(Subject)
class Subject(admin.ModelAdmin):
    list_display=['subject_name','standard']

