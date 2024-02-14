from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Category


class TestCategory(DetailView):
    template_name = 'categories/prepare_for_interview.html'
    context_object_name = 'category'
    slug_url_kwarg = 'category_slug'

    def get_object(self, queryset=None):
        return get_object_or_404(Category.objects, slug=self.kwargs[self.slug_url_kwarg])

