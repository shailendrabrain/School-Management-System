from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import StudentProfile, TeacherProfile

User = get_user_model()


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ("name", "enrollment", "standard")


class TeacherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfile
        fields = ("name",)
