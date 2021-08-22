# Generated by Django 2.2.10 on 2021-08-22 09:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210822_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='choice_answers',
            field=models.ManyToManyField(blank=True, related_name='answers', to='polls.AnswerChoice', verbose_name='Выбранные вариант(ы) ответа'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
