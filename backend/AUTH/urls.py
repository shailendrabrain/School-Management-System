from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views


urlpatterns = [
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("User/register/", views.UserRegister.as_view(), name="user_registraion"),
]
