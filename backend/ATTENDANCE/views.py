# THIS IF FILE FOR BUSSINESS LOGIC.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import SerializeAttendance,SerializeSubject,SerializeScore
from .models import Attendance,Subject


class AttendanceView(CreateAPIView):
    serializer_class=SerializeAttendance


class SubjectView(CreateAPIView):
    serializer_class=SerializeSubject    


class Attendance(ListAPIView):
    serializer_class=SerializeAttendance
    queryset=Attendance.objects.all()



class StudentScore(CreateAPIView):
    serializer_class=SerializeScore
        
    
    




