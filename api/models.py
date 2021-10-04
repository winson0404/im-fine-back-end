from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import USER_TYPES
import uuid
# Create your models here.


class User(AbstractUser):
    #TODO: change id to uuid afterwards
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    userType = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default="ADMIN"
    )

    phone_number = models.CharField(max_length=30, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name="admin_user")
    details = models.TextField(blank=True, default="")
    address = models.TextField( blank=True, default="")


class Regular(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, to_field="id")
    default_msg = models.TextField(blank=True, default="I am fine")
    meet_link = models.URLField(null=True)


class AdminLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    log_detail = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
