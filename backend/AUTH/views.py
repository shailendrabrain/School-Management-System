from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import StudentRegistrationSerializer, TeacherRegisterSerializer,UserRegisterSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class UserRegister(CreateAPIView):
    serializer_class=UserRegisterSerialize
    
    def post(self,request,format=None):
        serializer=UserRegisterSerialize(data=request.data)
        if serializer.is_valid():

            serializer.save()

            role=request.data.get('role')
            if role=='student':
                ser=StudentRegistrationSerializer(data=request.data)
                if ser.is_valid():
                    print("it is valid")
                


            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)





class StudentRegisterView(CreateAPIView):
    serializer_class = StudentRegistrationSerializer
    queryset = User.objects.all()


class TeacherRegisterView(CreateAPIView):
    serializer_class = TeacherRegisterSerializer
