from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser

from ..models import AnswerChoice
from ..serializers import AnswerChoiceCreateSerializer


class AnswerChoiceViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAdminUser,)
    serializer_class = AnswerChoiceCreateSerializer
    queryset = AnswerChoice.objects.all()
