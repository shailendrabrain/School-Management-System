from django.contrib.auth import get_user_model
from rest_framework import serializers
from ACCOUNT.models import StudentProfile
from ACCOUNT.serializers import StudentProfileSerializer

User = get_user_model()


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
