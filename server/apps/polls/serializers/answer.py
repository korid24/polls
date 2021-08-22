from typing import Final, Optional

from django.db import IntegrityError
from rest_framework import serializers

from ..models import Answer, AnswerChoice, Question
from .answer_choice import AnswerChoiceListSerializer


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Errors:
        SURVEY_NOT_ACTIVE: Final[str] = 'Опорос к которому принадлежит вопрос не активен'
        INVALID_CHOICE: Final[str] = 'Вариант ответа не относится к вопросу'
        INVALID_FREE_QUESTION_ANSWER: Final[str] = (
            'Ответ на вопрос с типом "ответ текстом" должен быть дан текстом'
        )
        INVALID_SINGLE_CHOICE_QUESTION_ANSWER: Final[str] = (
            'Ответ должен быть выбором единственного варианта'
        )
        INVALID_MULTIPLY_CHOICES_QUESTION_ANSWER: Final[str] = (
            'Ответ должен быть выбором одного или нескольких вариантов'
        )
        ADMINS_CANNOT_MAKE_ANSWERS: Final[str] = (
            'Администраторы не могут отвечать на вопросы'
        )
        USER_ALREADY_ANSWER_THIS_QUESTION: Final[str] = (
            'Пользователь уже отвечал на этот вопрос'
        )

    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.annotate_with_is_active(),
    )

    class Meta:
        model = Answer
        fields = ('id', 'question', 'text_answer', 'choice_answers')

    def to_internal_value(self, data: dict) -> dict:
        if self.partial:
            data.setdefault('question', self.instance.question.id)
            data.setdefault('text_answer', self.instance.text_answer)
            data.setdefault(
                'choice_answers',
                self.instance.choice_answers.values_list('id', flat=True),
            )

        data.setdefault('text_answer', None)
        data.setdefault('choice_answers', [])

        return super().to_internal_value(data)

    def validate_question(self, question: Question) -> Question:
        if not question.is_active:
            raise serializers.ValidationError(self.Errors.SURVEY_NOT_ACTIVE)

        return question

    def validate_choice_answers(
            self,
            choice_answers: Optional[list[AnswerChoice]],
    ) -> Optional[list[AnswerChoice]]:

        instance_question_id = self.instance.question_id if self.instance else None
        question_id = self.initial_data.get('question') or instance_question_id

        for choice_answer in choice_answers:
            if choice_answer.question_id != question_id:
                raise serializers.ValidationError(self.Errors.INVALID_CHOICE)

        return choice_answers

    def validate(self, attrs: dict) -> dict:
        question_type = attrs['question'].question_type
        text_answer = attrs['text_answer']
        choice_answers = attrs['choice_answers']

        user = self.context['request'].user

        if question_type == Question.QuestionTypes.FREE and (not text_answer or choice_answers):
            raise serializers.ValidationError(
                {'choice_answers': self.Errors.INVALID_FREE_QUESTION_ANSWER},
            )
        elif question_type == Question.QuestionTypes.SINGLE_CHOICE and (
                len(choice_answers) != 1
                or text_answer
        ):
            raise serializers.ValidationError(
                {'choice_answers': self.Errors.INVALID_SINGLE_CHOICE_QUESTION_ANSWER},
            )
        elif question_type == Question.QuestionTypes.MULTIPLY_CHOICES and (
                len(choice_answers) < 1
                or text_answer
        ):
            raise serializers.ValidationError(
                {'choice_answers': self.Errors.INVALID_MULTIPLY_CHOICES_QUESTION_ANSWER},
            )

        if user.is_authenticated and user.is_staff:
            raise serializers.ValidationError({'user': self.Errors.ADMINS_CANNOT_MAKE_ANSWERS})
        else:
            attrs['user'] = user if user.is_authenticated else None

        return attrs

    def save(self, **kwargs) -> Answer:
        try:
            return super().save(**kwargs)
        except IntegrityError:
            raise serializers.ValidationError(
                {'user': self.Errors.USER_ALREADY_ANSWER_THIS_QUESTION},
            )


class PassedSurveyAnswerSerializer(serializers.ModelSerializer):
    choice_answers = AnswerChoiceListSerializer(many=True)

    class Meta:
        model = Answer
        fields = ('id', 'text_answer', 'choice_answers')
