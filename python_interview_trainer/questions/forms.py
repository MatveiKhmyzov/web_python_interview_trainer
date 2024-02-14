from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.deconstruct import deconstructible

from python_interview_trainer.questions.models import Question


# class InterviewForm(forms.ModelForm):
