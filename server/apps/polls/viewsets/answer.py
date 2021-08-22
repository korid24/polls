from django.db.models import QuerySet
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission

from apps.core.permissions import IsNotAdminUser
from ..serializers import AnswerCreateSerializer
from ..models import Answer


class AnswerViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    serializer_class = AnswerCreateSerializer

    def get_permissions(self) -> list[BasePermission]:
        if self.action in {'update', 'partial_update'}:
            permission_classes = (IsAuthenticated, IsNotAdminUser)
        else:
            permission_classes = (IsNotAdminUser,)

        return [permission() for permission in permission_classes]

    def get_queryset(self) -> QuerySet:
        return Answer.objects.filter(user=self.request.user)
