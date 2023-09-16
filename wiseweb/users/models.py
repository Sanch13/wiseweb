from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    successful_logins = models.PositiveIntegerField(default=0)
    failed_logins = models.PositiveIntegerField(default=0)
