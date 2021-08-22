from django.db import models


class AnswerChoice(models.Model):
    question = models.ForeignKey(
        to='polls.Question',
        on_delete=models.CASCADE,
        related_name='answer_choices',
        verbose_name='Вопрос',
    )
    title = models.CharField(
        max_length=127,
        verbose_name='Текст ответа',
    )

    class Meta:
        verbose_name = 'Ответ на вопрос с выбором ответа'
        verbose_name_plural = 'Ответы на вопросы с выбором ответа'
