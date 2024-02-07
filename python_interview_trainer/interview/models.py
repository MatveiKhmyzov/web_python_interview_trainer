from django.db import models
from django.contrib.auth import get_user_model


class Question(models.Model):
    category = models.ForeignKey('InterviewCategory', on_delete=models.PROTECT, related_name='questions', verbose_name='Тема вопроса')
    question_text = models.TextField(blank=False, verbose_name='Формулировка вопроса')

    def __str__(self):
        return self.question_text


class QuestionChoice(models.Model):
    class Status(models.IntegerChoices):
        WRONG = 0, 'Неверный ответ'
        RIGHT = 1, 'Верный ответ'
    question = models.ManyToManyField('Question', blank=True, related_name='answers', verbose_name='Вопросы')
    choice = models.TextField(blank=False, verbose_name='Вариант ответа')
    is_right_choice = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)))

    def __str__(self):
        return self.choice


class InterviewCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.title


class UserAnswers(models.Model):
    user_id = models.ManyToManyField(get_user_model(), related_name='users', default=None)
    question_id = models.ForeignKey('Question', on_delete=models.CASCADE, blank=True, related_name='questions_for_user',
                                    verbose_name='Вопросы')
    choice = models.ForeignKey('QuestionChoice', on_delete=models.CASCADE, related_name='answers',
                               verbose_name='Ответы')
    time_create = models.DateTimeField(auto_now_add=True)
