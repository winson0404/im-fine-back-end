from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import USER_TYPES, HISTORY_TYPES, SOCIAL_PLATFORMS, MESSAGE_TYPES
import uuid
# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    userType = models.CharField(
        max_length=10,
        choices=USER_TYPES,
        default="ADMIN"
    )

    phone_number = models.CharField(max_length=30, null=True)
    friends = models.ManyToManyField('self')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Admin(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, to_field="id")
    details = models.TextField(blank=True, default="")
    address = models.TextField( blank=True, default="")


class Regular(models.Model):
    id = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, to_field="id")
    default_msg = models.TextField(blank=True, default="I am fine")
    meet_link = models.URLField(null=True)


# class FriendList(models.Model):
#     user_id = models.ForeignKey(Regular, on_delete=models.CASCADE, related_name="friend_list")
#     friend_id = models.ForeignKey(Regular, on_delete=models.SET_NULL, null=True)
#     friend_email = models.EmailField(default="", blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


class AdminLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Admin, on_delete=models.SET_NULL, null=True)
    log_detail = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(null=False)
    histType = models.CharField(
        max_length=10,
        choices=HISTORY_TYPES,
        null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    id = models.OneToOneField(History, primary_key=True, on_delete=models.CASCADE, to_field="id")
    platform = models.CharField(
        max_length=10,
        choices=SOCIAL_PLATFORMS,
        null=False
    )


class Message(models.Model):
    id = models.OneToOneField(History, primary_key=True, on_delete=models.CASCADE, to_field="id")
    receiver = models.CharField(max_length=50, null=False)
    messageType = models.CharField(
        max_length=10,
        choices=MESSAGE_TYPES,
        null=False
    )


# class TempHistory(models.Model):
#     content = models.TextField(null=False)
#     histType = models.CharField(
#         max_length=10,
#         choices=TEMP_HISTORY_TYPES,
#         null=False
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#     platform = models.CharField(
#         max_length=10,
#         choices=SOCIAL_PLATFORMS,
#         null=False
#     )
#     receiver = models.CharField(max_length=50, null=False)
#     messageType = models.CharField(
#         max_length=10,
#         choices=MESSAGE_TYPES,
#         null=False
#     )
