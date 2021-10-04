from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Admin, Regular, AdminLog, Message, Post, History
from .serializers import UserSerializer, AdminSerializer, RegularSerializer, AdminLogSerializer, HistorySerializer, PostSerializer, MessageSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_auth.registration.views import RegisterView


# Create your views here.

class CustomRegisterView(RegisterView):
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(id=response.data['user_id'])
        if user.userType == "ADMIN":
            user_type = "Admin"
            Admin.objects.create(id=user)
        else:
            user_type = "Regular"
            Regular.objects.create(id=user)
        custom_data = {"message": user_type + " user successfully created."}
        response.data.update(custom_data)
        return response


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


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class RegularViewSet(viewsets.ModelViewSet):
    queryset = Regular.objects.all()
    serializer_class = RegularSerializer


class AdminLogViewSet(viewsets.ModelViewSet):
    queryset = AdminLog.objects.all()
    serializer_class = AdminLogSerializer
    authentication_classes = (TokenAuthentication, )
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data._mutable = True
        request.data.update({"user_id": user.id})
        request.data._mutable = False
        response = super().create(request, *args, **kwargs)
        return response


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    authentication_classes = (TokenAuthentication, )

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data._mutable = True
        request.data.update({"user_id": user.id})
        request.data._mutable = False
        response = super().create(request, *args, **kwargs)

        history_type = response.data["histType"]
        history_id = response.data["id"]
        history = History.objects.get(id=history_id)
        #TODO: discuss to improve this
        if history_type == "POST":
            Post.objects.create(id=history)
        else:
            Message.objects.create(id=history)
        print("response data:", response.data)

        return response

    http_method_names = ['get', 'post', 'delete']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'delete']


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'delete']