from typing import Final

from django.db import models


class Question(models.Model):
    class QuestionTypes:
        FREE: Final[str] = 'free'
        SINGLE_CHOICE: Final[str] = 'single_choice'
        MULTIPLY_CHOICES: Final[str] = 'multiply_choices'

        CHOICES: Final[tuple[tuple[str, str], ...]] = (
            (FREE, 'Ответ текстом'),
            (SINGLE_CHOICE, 'Ответ с выбором одного варианта'),
            (MULTIPLY_CHOICES, 'Ответ с выбором нескольких вариантов'),
        )

    survey = models.ForeignKey(
        to='polls.Survey',
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='Опрос',
    )
    description = models.TextField(
        verbose_name='Текст вопроса',
    )
    question_type = models.CharField(
        max_length=16,
        choices=QuestionTypes.CHOICES,
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self) -> str:
        return self.description
