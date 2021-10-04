from django.db import transaction
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer
from .models import User, Admin, Regular, AdminLog
from .enums import USER_TYPES

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
            'updated_at': {'read_only': True}
        }


class AdminSerializer(serializers.ModelSerializer):

    class Meta:
        model = Admin
        fields = ("id", "address", "details")


class RegularSerializer(serializers.ModelSerializer):

    class Meta:
        model = Regular
        fields = ("id", "default_msg", "meet_link")


class AdminLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdminLog
        fields = ('id', 'user_id', 'log_detail', 'created_at')
        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True}
        }

