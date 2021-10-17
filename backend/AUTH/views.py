from rest_framework.generics import CreateAPIView, ListAPIView
from .models import CustomUser
from .serializers import UserSerialzer


class UserRegister(CreateAPIView):
    serializer_class = UserSerialzer
    queryset = CustomUser.objects.all()
