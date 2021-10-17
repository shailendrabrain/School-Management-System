from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
from ACCOUNT.models import StudentProfile


User = get_user_model()


class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        exclude = ["user"]


class UserSerialzer(serializers.ModelSerializer):
    profile = StudentProfileSerializer()

    class Meta:
        model = CustomUser
        fields = ["email", "role", "password", "profile"]

    def create(self, validated_data):
        profile = validated_data.pop("profile")

        user = super(UserSerialzer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()

        StudentProfile.objects.create(
            user=user,
            name=profile["name"],
            enrollment=profile["enrollment"],
            standard=profile["standard"],
        )

        return user

    def to_representation(self, instance):
        data = super(UserSerialzer, self).to_representation(instance)
        data.update(StudentProfileSerializer(StudentProfile.objects.get(user=instance)))
        return data
