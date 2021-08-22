from django.db import models


class Answer(models.Model):
    user = models.ForeignKey(
        to='users.BaseUser',
        on_delete=models.CASCADE,
        null=True,
        related_name='answers',
        verbose_name='Пользователь',
    )
    question = models.ForeignKey(
        to='polls.Question',
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='Вопрос',
    )
    text_answer = models.TextField(
        null=True,
        verbose_name='Ответ текстом',
    )
    choice_answers = models.ManyToManyField(
        to='polls.AnswerChoice',
        related_name='answers',
        blank=True,
        verbose_name='Выбранные вариант(ы) ответа',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время первого ответа',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Время последнего обновления ответа',
    )

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'
        constraints = (
            models.UniqueConstraint(
                fields=('user', 'question'),
                name='single_user_answer_by_question',
            ),
        )
