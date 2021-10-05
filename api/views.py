from rest_framework import viewsets, status, views
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Admin, Regular, AdminLog, Message, Post, History, FriendList
from .serializers import UserSerializer, AdminSerializer, RegularSerializer, AdminLogSerializer, HistorySerializer, \
    PostSerializer, MessageSerializer, FriendListSerializer
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
            response = {'message': username + " has been deleted"}
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {'message': e.args}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        response = {'message': "Please use the provided api/user/delete_user [DELETE] method"}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer


class RegularViewSet(viewsets.ModelViewSet):
    queryset = Regular.objects.all()
    serializer_class = RegularSerializer


class FriendListViewSet(viewsets.ModelViewSet):
    queryset = FriendList.objects.all()
    serializer_class = FriendListSerializer

    def create(self, request, *args, **kwargs):
        user = request.user
        # request.data._mutable = True
        request.data.update({"user_id": user.id})
        print(request.data)
        if request.data["friend_id"] is not None or request.data["friend_id"] == "":
            friend = User.objects.get(id=request.data["friend_id"])
            request.data.update({"friend_email": friend.email})
            request.data.update({"friend_username": friend.username})
        else:
            # check if both friend_id and email_id is empty
            if request.data["friend_email"] is None or request.data["friend_email"] == "":
                response = {'message': "must include either fried_email or friend_id"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        # request.data._mutable = False

        response = super().create(request, *args, **kwargs)
        return response


class AdminLogViewSet(viewsets.ModelViewSet):
    queryset = AdminLog.objects.all()
    serializer_class = AdminLogSerializer
    authentication_classes = (TokenAuthentication,)
    http_method_names = ['get', 'post']

    def create(self, request, *args, **kwargs):
        user = request.user
        request.data._mutable = True
        request.data.update({"user_id": user.id})
        request.data._mutable = False
        response = super().create(request, *args, **kwargs)
        return response


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all().order_by('-created_at')
    serializer_class = HistorySerializer
    authentication_classes = (TokenAuthentication,)

    http_method_names = ['get', 'post', 'delete']

    @action(detail=False, methods=['POST'])
    def make_history(self, request):
        user = request.user
        history_type = request.data["histType"]
        if history_type == "MESSAGE":
            history = History.objects.create(user_id=user, histType="MESSAGE", content=request.data["content"])
            Message.objects.create(id=history, messageType=request.data["messageType"],
                                   receiver=request.data["receiver"])
        elif history_type == "Post":
            history = History.objects.create(user_id=user, histType="POST", content=request.data["content"])
            Post.objects.create(id=history, platform=request.data["platform"])
        else:
            history1 = History.objects.create(user_id=user, histType="MESSAGE", content=request.data["content"])
            Message.objects.create(id=history1, mecssageType=request.data["messageType"],
                                   receiver=request.data["receiver"])
            history2 = History.objects.create(user_id=user, histType="POST", content=request.data["content"])
            Post.objects.create(id=history2, platform=request.data["platform"])

        response = {'message': 'history successfully made'}
        return Response(response, status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        response = {'message': "Please use the provided api/history/make_history [POST] method"}
        return Response(response, status=status.HTTP_403_FORBIDDEN)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'delete']


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    http_method_names = ['get', 'post', 'delete']
