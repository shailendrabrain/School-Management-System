from django.contrib import admin
from .models import Attendance, Subject
# Register your models here.

@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    pass


@admin.register(Subject)
class Subject(admin.ModelAdmin):
    pass
