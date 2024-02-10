from django.views.generic import ListView
from python_interview_trainer.categories.models import Category


class IndexView(ListView):
    model = Category
    template_name = 'base.html'
    title_page = 'Главная страница'
