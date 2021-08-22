from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
