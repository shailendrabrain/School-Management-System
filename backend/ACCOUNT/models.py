from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    name = models.CharField(max_length=128)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'tbl_teacher_profile'


class StudentProfile(models.Model):
    STANDARD = [
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=128)
    enrollment = models.CharField(max_length=10)
    standard = models.CharField(max_length=2, choices=STANDARD)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'tbl_student_profile'
