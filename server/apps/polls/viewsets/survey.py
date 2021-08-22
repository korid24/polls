from typing import Final, Type

from django.db.models import QuerySet
from rest_framework.permissions import AllowAny, IsAdminUser, BasePermission
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from ..models import Survey
from ..serializers import SurveySerializer, SurveyUpdateSerializer


class SurveyViewSet(ModelViewSet):
    SERIALIZERS_MAP: Final[dict[str, Type[ModelSerializer]]] = {
        'create': SurveySerializer,
        'update': SurveyUpdateSerializer,
        'partial_update': SurveyUpdateSerializer,
        'list': SurveySerializer,
    }

    def get_permissions(self) -> list[BasePermission]:
        if self.action in {'create', 'update', 'partial_update', 'destroy'}:
            permission_classes = (IsAdminUser,)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self) -> Type[ModelSerializer]:
        return self.SERIALIZERS_MAP[self.action]

    def get_queryset(self) -> QuerySet:
        return Survey.objects.all()
