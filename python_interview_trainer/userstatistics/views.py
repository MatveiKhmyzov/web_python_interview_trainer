from django.views.generic import ListView, CreateView
from python_interview_trainer.questions.models import Question
from python_interview_trainer.userstatistics.models import UserAnswers
from python_interview_trainer.userstatistics.forms import ExamForm
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import FormView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import FormMixin


class AnswerView(ListView, FormMixin):
    model = Question
    form_class = ExamForm
    template_name = 'questions/questions1.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'questions'
    paginate_by = 1

    def get_queryset(self):
        return Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_form_kwargs(self):
        """Passing the `choices` from your view to the form __init__ method"""

        kwargs = super().get_form_kwargs()
        questions = self.get_queryset()
        for i in range(len(questions)):
            answers = questions[i].answers.all()
            for answer in answers:
                # Here you can pass additional kwargs arguments to the form.
                kwargs.setdefault('answers', []).append((answer.question.all()[0].id, answer.choice))
        # print(self.kwargs)

        return kwargs

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        # Explicitly states what get to call:
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()
            # Here ou may consider creating a new instance of form_class(),
            # so that the form will come clean.

        # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        # Just include the form
        context = super(AnswerView, self).get_context_data(*args, **kwargs)
        context['form'] = self.form
        context['category'] = context['questions'][0].category
        return context


# class AnswerView(MultipleObjectMixin, FormView):
#     form_class = ExamForm
#     template_name = 'questions/questions1.html'
#     paginate_by = 1
#
#     def get_form_kwargs(self):
#         """Passing the `choices` from your view to the form __init__ method"""
#
#         kwargs = super().get_form_kwargs()
#         questions = Question.objects.filter(category__slug=self.kwargs['category_slug'])
#         for i in range(len(questions)):
#             answers = questions[i].answers.all()
#             for answer in answers:
#                 # Here you can pass additional kwargs arguments to the form.
#                 kwargs.setdefault('answers', []).append((answer.pk, answer.choice))
#         # print(self.kwargs)
#
#         return kwargs
#
#     def save(self, request, category_slug):
#         if request.method == 'POST':
#             form = ExamForm(request.POST)
#             print(form.initial)
#             if form.is_valid():
#                 print(form.initial)
#         else:
#             form = ExamForm(category_slug)
#
#         data = {
#             'title': 'Добавление статьи',
#             'form': form
#         }
#         return render(request, 'questions/questions1.html', data)


# class ShowQuestion(ListView):
#     model = Question
#     c
#     pk_url_kwarg = 'pk'
#     context_object_name = 'questions'
#     paginate_by = 1
#
#     def get_queryset(self):
#         return Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context['questions'])
#         context['category'] = context['questions'][0].category
#         return context
#
#
# class GetAnswer(CreateView):
#     template_name = 'questions/questions1.html'
#     form_class = ExamForm
#
#     def form_valid(self, form):
#         form.instance.user_id = self.request.user.id
#         form.instance.question_id = self.request.question.id
#         return super().form_valid(form)
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context['questions'])
#         context['category'] = context['questions'][0].category
#         return context
#
#     def get_queryset(self):
#         return Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')




# from django.http import HttpResponseRedirect
# from django.shortcuts import render
#
# from .forms import NameForm
#
# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})
