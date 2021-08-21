from django.contrib import admin

from ..models import BaseUser


@admin.register(BaseUser)
class BaseUserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username', 'is_superuser', 'date_joined')
