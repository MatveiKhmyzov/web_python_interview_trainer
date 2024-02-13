from django import template
from django.db.models import Count

from python_interview_trainer.questionchoices.models import QuestionChoice

register = template.Library()


# @register.inclusion_tag('questions/questions.html')
# def show_all_answers():
#     return {'answers': QuestionChoice.objects.all()}


@register.filter
def next_elem(some_list, current_index):
    try:
        return some_list[int(current_index) + 1]  # access the next element
    except:
        return ''


@register.filter
def previous_elem(some_list, current_index):
    try:
        return some_list[int(current_index) - 1]  # access the previous element
    except:
        return ''
