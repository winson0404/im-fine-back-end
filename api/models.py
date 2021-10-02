from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import USER_TYPES

# Create your models here.


class User(AbstractUser):
    #TODO: change id to uuid afterwards
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    userType = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default="ADMIN"
    )

    phone_number = models.CharField(max_length=30, null=True)



