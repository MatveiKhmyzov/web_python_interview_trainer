from django.db import models
from django.contrib.auth import get_user_model
from python_interview_trainer.questions.models import Question
from python_interview_trainer.questionchoices.models import QuestionChoice


class UserAnswers(models.Model):
    user_id = models.ManyToManyField(get_user_model(), related_name='users', default=None)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, blank=True, related_name='questions_for_user',
                                    verbose_name='Вопросы')
    choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, related_name='answers',
                               verbose_name='Ответы')
    time_create = models.DateTimeField(auto_now_add=True)
