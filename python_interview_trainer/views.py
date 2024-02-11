from django.views.generic import ListView
from python_interview_trainer.categories.models import Category


class IndexView(ListView):
    model = Category
    template_name = 'categories/index_category.html'
    context_object_name = 'categories'
    title_page = 'Категории тестов'
