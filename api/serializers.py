from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer
from .models import User, Admin, Regular, AdminLog, History, Post, Message, FriendList, Announcement, Notification
from .enums import USER_TYPES, MESSAGE_TYPES, SOCIAL_PLATFORMS


# custom register credentials


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user_id')


class CustomRegisterSerializer(RegisterSerializer):
    userType = serializers.ChoiceField(choices=USER_TYPES)
    phone_number = serializers.CharField(max_length=30, required=False)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.userType = self.data.get('userType')
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ("id", "username", "email", "password", "userType", "created_at", "updated_at")
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


class SimpleUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class FriendListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendList
        fields = ('user_id', 'friend_id', 'friend_email', 'friend_username')
        extra_kwargs = {
            'user_id': {'write_only': True, 'required': True},
        }


class RegularSerializer(serializers.ModelSerializer):
    friend_list = FriendListSerializer(many=True)
    user_detail = SimpleUserSerializer(source='id', many=False)

    class Meta:
        model = Regular
        fields = ("id", "user_detail", "default_msg", "meet_link", "friend_list")


class AdminSerializer(serializers.ModelSerializer):
    user_detail = SimpleUserSerializer(source='id', many=False)

    class Meta:
        model = Admin
        fields = ("id", "user_detail", "address", "details")


class AdminLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminLog
        fields = ('id', 'user_id', 'log_detail', 'created_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
        }


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ("id", "user_id", "histType", "created_at", "content")
        extra_kwargs = {
            'created_at': {'read_only': True}
        }


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "platform")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "receiver", "messageType")


class AnnouncementSerializer(serializers.ModelSerializer):
    sender = AdminSerializer(source='sender_id', many=False, read_only=True)

    class Meta:
        model = Announcement
        fields = ("id", "sender", "content", "created_at")


class NotificationSenderSerializer(serializers.ModelSerializer):
    user_detail = SimpleUserSerializer(source='id', many=False)

    class Meta:
        model = Regular
        fields = ("id", "user_detail")


class NotificationSerializer(serializers.ModelSerializer):
    sender = NotificationSenderSerializer(source='sender_id', many=False, read_only=True)

    class Meta:
        model = Notification
        fields = ("receiver_id", "sender", "content", "created_at")
