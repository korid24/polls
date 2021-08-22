from django_filters import rest_framework as rest_filters

from ..models import Question


class QuestionFilterSet(rest_filters.FilterSet):
    survey_id = rest_filters.NumberFilter()

    class Meta:
        model = Question
        fields = ('survey_id',)
