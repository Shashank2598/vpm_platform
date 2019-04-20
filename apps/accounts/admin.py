from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.accounts import models as auth_models


class CustomUserAdmin(UserAdmin):

    list_display = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    add_fieldsets = (
        (None, {
            'fields': ('email', 'first_name', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(auth_models.BaseUser, CustomUserAdmin)