from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import StudentRegistrationSerializer

User = get_user_model()


class StudentRegisterView(CreateAPIView):
    serializer_class = StudentRegistrationSerializer
    queryset = User.objects.all()
