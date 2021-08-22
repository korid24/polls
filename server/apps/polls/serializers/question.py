from rest_framework import serializers

from .answer_choice import AnswerChoiceListSerializer
from .survey import SurveyBaseSerializer
from ..models import Question


class QuestionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'description')


class QuestionCreateSerializer(QuestionListSerializer):
    class Meta(QuestionListSerializer.Meta):
        fields = QuestionListSerializer.Meta.fields + ('survey', 'question_type')


class QuestionRetrieveSerializer(QuestionCreateSerializer):
    answer_choices = AnswerChoiceListSerializer(many=True)
    survey = SurveyBaseSerializer()

    class Meta(QuestionCreateSerializer.Meta):
        fields = QuestionCreateSerializer.Meta.fields + ('answer_choices',)
