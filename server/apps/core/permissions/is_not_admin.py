from django.views import View
from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsNotAdminUser(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return not (request.user.is_authenticated and request.user.is_staff)
