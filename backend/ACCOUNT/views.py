from django.shortcuts import render
from django.contrib.auth import get_user_model, authenticate
from .models import StudentProfile,TeacherProfile
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentSerialzer
from rest_framework.generics import CreateAPIView, ListAPIView
User=get_user_model()


class RegisterView(CreateAPIView):
    serializer_class=StudentSerialzer
    queryset=StudentProfile.objects.all()



