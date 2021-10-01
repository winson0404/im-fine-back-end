from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['GET'])
    def profile(self, request, pk=None):
        try:
            userdata = User.objects.get(id=pk)
            return Response(UserSerializer(request.user).data, status=status.HTTP_200_OK)
        except:
            response = {'message': 'No token provided'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
