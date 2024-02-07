from django.db import models
from python_interview_trainer.questions.models import Question


class QuestionChoice(models.Model):
    class Status(models.IntegerChoices):
        WRONG = 0, 'Неверный ответ'
        RIGHT = 1, 'Верный ответ'
    question = models.ManyToManyField(Question, blank=True, related_name='answers', verbose_name='Вопросы')
    choice = models.TextField(blank=False, verbose_name='Вариант ответа')
    is_right_choice = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)))

    def __str__(self):
        return self.choice
