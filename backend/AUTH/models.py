from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ROLES = [
        ('student', 'STUDENT'),
        ('teacher', 'TEACHER'),
        ('admin', 'ADMIN'),
    ]

    username = None
    first_name = None
    last_name = None
    email = models.EmailField(max_length=254, unique=True)
    role = models.CharField(max_length=10, choices=ROLES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def create_user(self):
        pass

    class Meta:
        db_table = 'tbl_user'
        verbose_name = 'User'
        ordering = ['-date_joined']
