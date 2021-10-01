from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.


class User(AbstractUser):

    class UserType(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        REGULAR = "REGULAR", _("Regular User")

    userType = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.ADMIN
    )



