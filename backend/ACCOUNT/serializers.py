from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import StudentProfile, TeacherProfile

User = get_user_model()


class StudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ["user", "name", "enrollment", "standard"]
