from .models import UserAnswers
from django import forms
from django.utils.translation import gettext as _
from python_interview_trainer.userstatistics.models import UserAnswers
from python_interview_trainer.questions.models import Question
from django.core.paginator import Paginator


class ExamForm(forms.Form):
    # class Meta:
    #     model = UserAnswers
    #     fields = ['choice']
    #
    # user_id = None
    # question_id = None

    def __init__(self, *args, **kwargs):
        """Displaying first question with answers on form"""

        question = kwargs.pop('question')
        super(ExamForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.ModelChoiceField(queryset=question.answers.all(),
                                                       widget=forms.RadioSelect, required=True)
