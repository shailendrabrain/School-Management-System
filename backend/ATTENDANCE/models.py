from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from ACCOUNT.models import StudentProfile

User=get_user_model()

def today_date():
    return datetime.today().date()


class Subject(models.Model):
    STANDARD = [
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]
    subject_name=models.CharField(max_length=70)
    standard=models.CharField(max_length=2,choices=STANDARD)

    def __str__(self):
        return self.subject_name

        


class Attendance(models.Model):
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='student_attendance')
    date=models.DateField(default=today_date)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='subject_attendance')
    

    def __str__(self):
        return str(self.student)



class Score(models.Model):
    date=models.DateField(default=today_date);
    student=models.ForeignKey(StudentProfile,on_delete=models.CASCADE,related_name='Student_name')
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='Subject')
    mark=models.PositiveIntegerField()
    total_score=models.PositiveIntegerField()


    def __str__(self):
        return str(self.student)
