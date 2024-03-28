from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from python_interview_trainer.questions.models import Question
from python_interview_trainer.questionchoices.models import QuestionChoice


class UserAnswers(models.Model):
    user_id = models.ManyToManyField(get_user_model(), related_name='users', default=None)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions_for_user',
                                    verbose_name='Вопросы')
    choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, related_name='answers',
                               verbose_name='Ответы')
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Results of interview for theme "{self.question_id.category}"'

    def get_absolute_url(self):
        return reverse('getting_result', kwargs={'category_slug': self.question_id.category})
