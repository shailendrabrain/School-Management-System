from django.urls import path
from . import views

urlpatterns=[
            path('student/attendance/',views.AttendanceView.as_view(),name='student_attendance'),
            path('subject/',views.SubjectView.as_view(),name='subject'),
            path('getattendance/',views.Attendance.as_view(),name='attendance')
]
