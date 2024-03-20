from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Category
from python_interview_trainer.questions.models import Question


class TestCategory(DetailView):
    template_name = 'categories/prepare_for_interview.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Category.objects, slug=self.kwargs[self.slug_url_kwarg])

    def get_context_data(self, **kwargs):
        context = super(TestCategory, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(category__slug=context['category'].slug)
        context['start_question'] = context['questions'][0]
        return context



