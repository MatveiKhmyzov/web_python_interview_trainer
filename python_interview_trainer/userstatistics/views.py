from datetime import datetime

from django.views.generic import ListView, CreateView, DetailView
from python_interview_trainer.questions.models import Question
from python_interview_trainer.userstatistics.models import UserAnswers
from python_interview_trainer.userstatistics.forms import ExamForm
from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import FormView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import FormMixin
from django.shortcuts import render, get_object_or_404


class AnswerView(DetailView, FormMixin):
    form_class = ExamForm
    template_name = 'questions/questions1.html'
    context_object_name = 'question'
    pk_url_kwarg = 'pk'
    paginate_by = 1

    def get_object(self, queryset=None):
        return get_object_or_404(Question, pk=self.kwargs[self.pk_url_kwarg])

    def get_queryset(self):
        return Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')

    def get_form_kwargs(self):
        """Passing the `choices` from your view to the form __init__ method"""

        kwargs = super(AnswerView, self).get_form_kwargs()
        question = self.get_object()
        kwargs['question'] = question
        # kwargs['other_questions'] = self.get_queryset()[1:]
        return kwargs

    @staticmethod
    def get_generator_next_previous_elem(collection, elem_on_page):
        collection_len = len(collection)
        count = 0
        if collection_len > 1:
            for i in range(len(collection)):
                count += 1
                if collection[i] == elem_on_page and i == 0:
                    return None, collection[i+1]
                elif (collection[i] == elem_on_page or count == collection_len) and i == collection_len - 1:
                    return collection[i - 1], None
                elif collection[i] == elem_on_page:
                    return collection[i-1], collection[i+1]


        else:
            return None, None

    def get_context_data(self, *args, **kwargs):
        # Just include the form
        context = super(AnswerView, self).get_context_data(**kwargs)
        # context['form'] = self.form
        all_questions = self.get_queryset()
        question_on_page = self.get_object()
        # print(all_questions, question_on_page)
        previous_question, next_question = self.get_generator_next_previous_elem(all_questions, question_on_page)
        # print(previous_question, next_question)
        context['category'] = context['question'].category
        context['previous_question'] = previous_question
        context['next_question'] = next_question
        # context['question_number_in_lst'] = count
        # context['next_questions'] = self.get_queryset()[list(self.get_queryset()).index(context['question'])+1:]
        # context['previous_questions'] = self.get_queryset()[:list(self.get_queryset()).index(context['question'])]
        # print(context)
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # When the form is submitted, it will enter here
        if request.method == 'POST':
            user_id = request.user.id
            question_id = Question.objects.get(pk=kwargs['pk']).id
            choice = request.POST.get('choice')
            time_create = datetime.now()
            user_answer = UserAnswers.objects.create(question_id_id=question_id, choice_id=choice,
                                                     time_create=time_create)
            user_answer.user_id.add(user_id)
            user_answer.save()
            form = self.get_form(self.form_class)
            # print(form)

            # if form.is_valid():
            #     print()
            #     obj = form.save()
            #     request.user.users.add(user_answer)
            #     # user_answer.user_id.add(user_id)
            #     print(obj.id)
            #     obj.save()

                # Here ou may consider creating a new instance of form_class(),
                # so that the form will come clean.

            # Whether the form validates or not, the view will be rendered by get()
        return self.get(request, *args, **kwargs)


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
