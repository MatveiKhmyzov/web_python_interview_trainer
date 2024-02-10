from django.shortcuts import render
from django.views.generic import ListView
from .models import Category


class TestCategory(ListView):
    model = Category
    template_name = 'categories/index_category.html'
    context_object_name = 'categories'
    title_page = 'Категории тестов'

