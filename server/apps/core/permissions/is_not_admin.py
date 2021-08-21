from django.views import View
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request


class IsNotAdminUser(IsAuthenticated):
    def has_permission(self, request: Request, view: View) -> bool:
        return super().has_permission(request, view) and not request.user.is_staff
