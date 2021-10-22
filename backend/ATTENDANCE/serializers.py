from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Attendance,Subject
User=get_user_model()


class SerializeAttendance(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=['student','date','subject']



class SerializeSubject(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields=['subject_name','standard']
                

