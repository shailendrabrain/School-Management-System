from django.urls import path
from . import views

urlpatterns = [
path('student/standard/<int:pk>',views.StudentByStandard.as_view()),
path('student/',views.Student.as_view()),
path('student/attendance/<int:enroll_number',views.AttendanceOfStudent.as_view())
]
