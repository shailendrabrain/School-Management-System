from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path("register/student/", views.StudentRegisterView.as_view(), name='register_student'),
    path("register/teacher/", views.TeacherRegisterView.as_view(), name="teacher_register"),
    path('register/user/',views.UserRegister.as_view(),name='userregister'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
