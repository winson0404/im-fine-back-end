from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
# from rest_framework.decorators import schema

from .views import UserViewSet, AdminViewSet, RegularViewSet, CustomRegisterView, AdminLogViewSet, HistoryViewSet, \
    PostViewSet, MessageViewSet, FriendListViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('admins', AdminViewSet)
router.register('regulars', RegularViewSet)
router.register('admin_logs', AdminLogViewSet)
router.register('history', HistoryViewSet)
router.register('post', PostViewSet)
router.register('message', MessageViewSet)
router.register('friend_connections', FriendListViewSet)

# disable some endpoints
# (vf, app_name, namespace) = include('rest_auth.urls')
# vf.LoginView = schema(None)(vf.LoginView)
# vf.LoginView = schema(None)(vf.LogoutView)
# vf.LoginView = schema(None)(vf.PasswordChangeView)
# vf.LoginView = schema(None)(vf.PasswordResetConfirmView)
# vf.LoginView = schema(None)(vf.PasswordResetView)
# vf.LoginView = schema(None)(vf.UserDetailsView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    url(r'^account/', include('allauth.urls')),
    path('auth/register/', CustomRegisterView.as_view(), name='custom_registration'),
]
