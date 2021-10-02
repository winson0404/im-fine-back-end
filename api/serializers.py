from django.db import transaction
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import User
from .enums import USER_TYPES


# custom register credentials
class CustomRegisterSerializer(RegisterSerializer):

    userType = serializers.ChoiceField(choices=USER_TYPES)
    phone_number = serializers.CharField(max_length=30, required=False)

    # Define transaction.atomic to rollback the save operation in case of error
    @transaction.atomic
    def save(self, request):
        print("user data", self.data)
        user = super().save(request)
        user.userType = self.data.get('userType')
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "userType")
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
