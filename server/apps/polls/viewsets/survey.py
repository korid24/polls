from typing import Final

from django.db.models import QuerySet
from rest_framework.permissions import IsAdminUser, BasePermission
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from apps.core.permissions import IsNotAdminUser
from ..models import Survey
from ..serializers import SurveyCreateSerializer


class SurveyViewSet(ModelViewSet):
    SERIALIZERS_MAP: Final[dict[str, ModelSerializer]] = {
        'create': SurveyCreateSerializer,
        'update': SurveyCreateSerializer,
        'partial_update': SurveyCreateSerializer,
    }

    def get_permissions(self) -> list[BasePermission]:
        if self.action in {'create', 'update', 'partial_update', 'delete'}:
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (IsNotAdminUser,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self) -> ModelSerializer:
        return self.SERIALIZERS_MAP[self.action]

    def get_queryset(self) -> QuerySet:
        return Survey.objects.all()
