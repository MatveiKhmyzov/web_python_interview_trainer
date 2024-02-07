# Generated by Django 4.2.1 on 2024-02-06 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Формулировка вопроса')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='interview.interviewcategory', verbose_name='Тема вопроса')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.TextField(verbose_name='Вариант ответа')),
                ('is_right_choice', models.BooleanField(choices=[(False, 'Неверный ответ'), (True, 'Верный ответ')])),
                ('question', models.ManyToManyField(blank=True, related_name='questions', to='interview.question', verbose_name='Вопросы')),
            ],
        ),
        migrations.CreateModel(
            name='UserAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('choice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='interview.questionchoice', verbose_name='Ответы')),
                ('question_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions_for_user', to='interview.question', verbose_name='Вопросы')),
                ('user_id', models.ManyToManyField(default=None, related_name='users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
