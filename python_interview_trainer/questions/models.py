from django.db import models
from python_interview_trainer.categories.models import Category


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='questions',
                                 verbose_name='Тема вопроса')
    question_text = models.TextField(blank=False, verbose_name='Формулировка вопроса')

    def __str__(self):
        return self.question_text
