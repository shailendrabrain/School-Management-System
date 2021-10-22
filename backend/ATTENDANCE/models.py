from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from ACCOUNT.models import StudentProfile

User=get_user_model()

def today_date():
    return datetime.today().date()


class Subject(models.Model):
    subject_name=models.CharField(max_length=70)
    standard=models.PositiveIntegerField()

    def __str__(self):
        return self.subject_name

        


class Attendance(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='student_attendance')
    date=models.DateField(default=today_date)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject_attendance')
    

    def __str__(self):
        return str(self.student)

