from django.urls import path
from rest_framework import routers
from django.conf.urls import include, url
# from rest_framework.decorators import schema

from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)

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
    path('auth/register/', include('rest_auth.registration.urls')),
]