from django.views.generic import ListView
from python_interview_trainer.categories.models import Category
from django.http import HttpResponse, HttpResponseNotFound


class IndexView(ListView):
    model = Category
    template_name = 'categories/index_category.html'
    context_object_name = 'categories'
    extra_context = {'title':'Главная страница'}


def contact(request):
    return HttpResponse('Обратная связь')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
