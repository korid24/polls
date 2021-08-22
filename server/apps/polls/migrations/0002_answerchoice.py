# Generated by Django 2.2.10 on 2021-08-22 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127, verbose_name='Текст ответа')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_choices', to='polls.Question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ на вопрос с выбором ответа',
                'verbose_name_plural': 'Ответы на вопросы с выбором ответа',
            },
        ),
    ]
