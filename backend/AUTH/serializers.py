from django.contrib.auth import get_user_model
from rest_framework import serializers
from ACCOUNT.models import StudentProfile,TeacherProfile
from .models import CustomUser
from ACCOUNT.serializers import StudentProfileSerializer,TeacherProfileSerializer

User = get_user_model()

class UserRegisterSerialize(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        exclude=()




class StudentRegistrationSerializer(serializers.ModelSerializer):
    profile = StudentProfileSerializer(source='student_profile')

    class Meta:
        model = User
        fields = ['email', 'password', 'profile']

    def create(self, validated_data):
        profile = validated_data.pop('student_profile')
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.role = 'student'
        user.save()
        profile = StudentProfile.objects.create(user=user, **profile)
        profile.save()
        return user


class TeacherRegisterSerializer(serializers.ModelSerializer):
    profile=TeacherProfileSerializer(source='teacher_profile')
    class Meta:
        model=User
        fields=['email','password','profile']

    def create(self, validated_data):
        profile=validated_data.pop('teacher_profile')
        user=User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        profile=TeacherProfile.objects.create(user=user,**profile)
        profile.save()
        return user  
    
