from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import StudentProfile
from django.http import Http404
from rest_framework.response import Response
from  .serializers import StudentProfileSerializer
from .models import StudentProfile

from ATTENDANCE.models import  Attendance
from ATTENDANCE.serializers import SerializeAttendance
User = get_user_model()


class StudentByStandard(ListAPIView):

    serializer_class=StudentProfileSerializer

    def get_queryset(self):
        standard=self.kwargs['pk']
        return StudentProfile.objects.filter(standard=standard)

    

class Student(ListAPIView):
    serializer_class=SerializeAttendance
    queryset=StudentProfile.objects.all()




class AttendanceOfStudent(ListAPIView):
    # serializer_class=SerializeAttendance

    def get(self, request, enroll_number, **kwargs):
        student=StudentProfile.object.get(enrollment=enroll_number)
        user_name=student['user']
        student_attendance=Attendance.object.filter(student=user_name)
        ser=SerializeAttendance(student_attendance)
        return Response(ser.data)



            
        


    



    

