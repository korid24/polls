from typing import Final, Type

from django.db.models import QuerySet, Prefetch
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAdminUser, BasePermission, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from ..models import Survey, Answer
from ..serializers import SurveySerializer, SurveyUpdateSerializer, SurveyRetrieveSerializer
from ...core.permissions import IsNotAdminUser


class SurveyViewSet(ModelViewSet):
    SERIALIZERS_MAP: Final[dict[str, Type[ModelSerializer]]] = {
        'create': SurveySerializer,
        'update': SurveyUpdateSerializer,
        'partial_update': SurveyUpdateSerializer,
        'list': SurveySerializer,
        'passed_surveys': SurveySerializer,
        'retrieve': SurveyRetrieveSerializer,
    }

    def get_permissions(self) -> list[BasePermission]:
        if self.action in {'create', 'update', 'partial_update', 'destroy'}:
            permission_classes = (IsAdminUser,)
        elif self.action in {'passed_surveys', 'retrieve'}:
            permission_classes = (IsAuthenticated, IsNotAdminUser)
        else:
            permission_classes = (AllowAny,)

        return [permission() for permission in permission_classes]

    def get_serializer_class(self) -> Type[ModelSerializer]:
        return self.SERIALIZERS_MAP[self.action]

    def get_queryset(self) -> QuerySet:
        queryset = Survey.objects.annotate_with_is_active()

        if (
                not (self.request.user and self.request.user.is_staff)
                and self.action not in {'passed_surveys', 'retrieve'}
        ):
            queryset = queryset.filter(
                is_active=True,
            )

        if self.action in {'passed_surveys', 'retrieve'}:
            queryset = queryset.annotate_with_is_passed(
                user_id=self.request.user.id,
            ).filter(
                is_passed=True,
            )

        if self.action == 'retrieve':
            queryset = queryset.prefetch_related(
                'questions',
                Prefetch(
                    lookup='questions__answers',
                    queryset=Answer.objects.filter(user=self.request.user),
                ),
            )

        return queryset

    @action(methods=('GET',), detail=False, url_path='passed-surveys')
    def passed_surveys(self, request: Request, *args, **kwargs) -> Response:
        return super().list(request, *args, **kwargs)
