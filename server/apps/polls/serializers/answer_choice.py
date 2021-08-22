from typing import Final

from rest_framework import serializers

from ..models import AnswerChoice, Question


class AnswerChoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerChoice
        fields = ('id', 'title')


class AnswerChoiceCreateSerializer(AnswerChoiceListSerializer):
    class Errors:
        WRONG_QUESTION_TYPE: Final[str] = (
            'Нельзя создать вариант ответа для вопроса с ответом текстом'
        )

    class Meta(AnswerChoiceListSerializer.Meta):
        fields = AnswerChoiceListSerializer.Meta.fields + ('question',)

    def validate_question(self, question: Question) -> Question:
        if question.question_type == Question.QuestionTypes.FREE:
            raise serializers.ValidationError(self.Errors.WRONG_QUESTION_TYPE)

        return question
