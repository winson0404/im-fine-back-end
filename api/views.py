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

    http_method_names = http_method_names = ['get', 'delete', 'put']

    @action(detail=True, methods=['DELETE'])
    def delete_user(self, request, pk=None):
        try:
            user = User.objects.get(id=pk)
            username = user.username
            user.delete()
            response = {'message': username+" has been deleted"}
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {'message': e.args}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        return Response("You are not allowed to do this", status=status.HTTP_401_UNAUTHORIZED)
