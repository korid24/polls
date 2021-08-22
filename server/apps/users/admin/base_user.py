from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..models import BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name', 'username', 'is_superuser', 'date_joined')
