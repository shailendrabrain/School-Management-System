from django.contrib import admin
from .models import StudentProfile,TeacherProfile


@admin.register(StudentProfile)
class Studentprofile(admin.ModelAdmin):
    pass


@admin.register(TeacherProfile)
class Teacherprofile(admin.ModelAdmin):
    pass
