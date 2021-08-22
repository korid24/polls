from typing import Type, Final

from django.db.models import QuerySet
from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from rest_framework.permissions import AllowAny, IsAdminUser, BasePermission

from ..filters import QuestionFilterSet
from ..models import Question
from ..serializers import (
    QuestionCreateSerializer,
    QuestionListSerializer,
    QuestionRetrieveSerializer,
)


class QuestionViewSet(ModelViewSet):
    filterset_class = QuestionFilterSet

    SERIALIZERS_MAP: Final[dict[str, Type[ModelSerializer]]] = {
        'create': QuestionCreateSerializer,
        'update': QuestionCreateSerializer,
        'partial_update': QuestionCreateSerializer,
        'list': QuestionListSerializer,
        'retrieve': QuestionRetrieveSerializer,
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
        queryset = Question.objects.all()

        if self.action == 'retrieve':
            queryset = queryset.select_related('survey').prefetch_related('answer_choices')

        return queryset
