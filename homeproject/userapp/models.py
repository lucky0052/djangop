from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import UserManager

class CustomUser(AbstractUser):
    """User model."""

    email = models.EmailField(unique=True)
    profile_img = models.ImageField(upload_to="profile")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


