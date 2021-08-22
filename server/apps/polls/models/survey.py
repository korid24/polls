from django.db import models


class Survey(models.Model):
    name = models.CharField(
        max_length=127,
        verbose_name='Название',
    )
    start_date = models.DateField(
        verbose_name='Дата начала',
    )
    end_date = models.DateField(
        verbose_name='Дата окончания',
    )
    description = models.TextField(
        verbose_name='Описание',
    )

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self) -> str:
        return self.name
