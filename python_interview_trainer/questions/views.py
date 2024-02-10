from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from python_interview_trainer.questions.models import Question


class ShowQuestion(DetailView):
    model = Question
    template_name = 'questions/questions.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'question'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['answers'] = Question.objects.filter(answers__pk=self.kwargs['pk']).select_related('cat')
    #     return context

    def get_object(self, queryset=None):
        return get_object_or_404(Question.objects, pk=self.kwargs[self.pk_url_kwarg])
