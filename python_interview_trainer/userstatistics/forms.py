from .models import UserAnswers
from django import forms
from django.utils.translation import gettext as _
from python_interview_trainer.userstatistics.models import UserAnswers
from python_interview_trainer.questions.models import Question
from django.core.paginator import Paginator


class ExamForm(forms.ModelForm):
    class Meta:
        model = UserAnswers
        fields = ['choice']

    user_id = None
    question_id = None

    def __init__(self, *args, **kwargs):
        """Populating the choices of  the favorite_choices field using the favorites_choices kwargs"""
        # self.user_id = user
        # self.question_id = Question.objects.filter(user=self.user)
        question = kwargs.pop('question')
        # other_questions = kwargs.pop('other_questions')
        super(ExamForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = forms.ModelChoiceField(queryset=question.answers.all(),
                                                       widget=forms.RadioSelect, required=False)
        # print(other_questions)

# class ExamForm(forms.Form):
#     def __init__(self, category_slug):
#         super(ExamForm, self).__init__()
#         questions = Question.objects.filter(category__slug=category_slug)
#         for i in range(len(questions)):
#             choices = []
#             answers = questions[i].answers.all()
#             for answer in answers:
#                 choices.append((answer.pk, answer.choice))
#                 self.fields["question_%d" % questions[i].pk] = forms.ChoiceField(label=questions[i].question_text,
#                                                                              required=True,
#                                                                              choices=choices,
#                                                                              widget=forms.CheckboxSelectMultiple)

# class QuestionForm(forms.ModelForm):
#     model = Question
#     choices = forms.MultipleChoiceField(required=True)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#     class Meta:
#         model = UserAnswers
#         fields = ['choice']
