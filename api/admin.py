from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Admin, Regular, AdminLog


class CustomUserAdmin(UserAdmin):

    model = User

    # for django admin only (can remove afterwards but keep it for now to be safe)
    # list_display = (
    #     'username', 'email', 'first_name', 'last_name', 'userType'
    # )
    # fieldsets = (
    #     (None, {
    #         'fields': ('username', 'password')
    #     }),
    #     ('Personal info', {
    #         'fields': ('first_name', 'last_name', 'email')
    #     }),
    #     ('Permissions', {
    #         'fields': (
    #             'is_active', 'is_staff', 'is_superuser',
    #             'groups', 'user_permissions'
    #         )
    #     }),
    #     ('Important dates', {
    #         'fields': ('last_login', 'date_joined')
    #     }),
    #     ('Additional info', {
    #         'fields': ('userType',)
    #     })
    # )
    # add_fieldsets = (
    #     (None, {
    #         'fields': ('username', 'password1', 'password2')
    #     }),
    #     ('Personal info', {
    #         'fields': ('first_name', 'last_name', 'email')
    #     }),
    #     ('Permissions', {
    #         'fields': (
    #             'is_active', 'is_staff', 'is_superuser',
    #             'groups', 'user_permissions'
    #         )
    #     }),
    #     ('Important dates', {
    #         'fields': ('last_login', 'date_joined')
    #     }),
    #     ('Additional info', {
    #         'fields': ('userType',)
    #     })
    # )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Admin)
admin.site.register(Regular)
admin.site.register(AdminLog)
