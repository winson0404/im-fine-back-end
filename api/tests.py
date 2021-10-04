from django.test import TestCase
import json
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import UserSerializer

# Create your tests here.
class RegistrationTestCase(APITestCase):

    def test_registration(self):
        data = {
            "username": "weixiong0404",
            "email": "winson@winson.com",
            "password1": "Admin.123",
            "password2": "Admin.123",
            "userType": "ADMIN"}
        response = self.client.post("/api/auth/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
