from django import template
from django.db.models import Count

from python_interview_trainer.questionchoices.models import QuestionChoice
from utils import menu

register = template.Library()


@register.simple_tag()
def get_menu():
    return menu
