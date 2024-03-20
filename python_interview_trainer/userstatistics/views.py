from datetime import datetime

from django.views.generic import DetailView
from python_interview_trainer.questions.models import Question
from python_interview_trainer.userstatistics.models import UserAnswers
from python_interview_trainer.userstatistics.forms import ExamForm
from django.views.generic.edit import FormMixin
from django.shortcuts import get_object_or_404
from django.views.generic import FormView


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
        """Passing the first question from view to the form __init__ method"""

        kwargs = super(AnswerView, self).get_form_kwargs()
        question = self.get_object()
        kwargs['question'] = question

        return kwargs

    @staticmethod
    def get_generator_next_previous_elem(collection, elem_on_page):
        """Getting previous and next elements of collection by based on current element of page"""

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
        """Getting context data for question page"""

        context = super(AnswerView, self).get_context_data(**kwargs)
        all_questions = self.get_queryset()
        question_on_page = self.get_object()
        print(question_on_page.id)
        previous_question, next_question = self.get_generator_next_previous_elem(all_questions, question_on_page)
        context['question'] = question_on_page
        context['category'] = context['question'].category
        context['previous_question'] = previous_question
        context['next_question'] = next_question
        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        """Simple saving of form data """

        user_id = request.user.id
        question = Question.objects.get(pk=kwargs['pk'])
        choice = request.POST.get('choice')
        time_create = datetime.now()
        # form = ExamForm(request.POST, question=question)
        # if form.is_valid():
        #     try:
        user_answer = UserAnswers.objects.create(question_id_id=question.id, choice_id=choice,
                                                             time_create=time_create)
        user_answer.user_id.add(user_id)
        # print(user_answer)
            # except:
            #     form.add_error(None, 'Ошибка сохранения ответа в базу данных')
        # form = self.get_form(self.form_class)
        return self.get(request, *args, **kwargs)
