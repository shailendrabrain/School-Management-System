from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    path("register/student/", views.StudentRegisterView.as_view(), name='register_student'),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]
