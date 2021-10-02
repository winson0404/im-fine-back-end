from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import USER_TYPES

# Create your models here.


class User(AbstractUser):

    userType = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default="ADMIN"
    )



