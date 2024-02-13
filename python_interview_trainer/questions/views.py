from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from python_interview_trainer.questions.models import Question
from django.core.paginator import Paginator
from python_interview_trainer.categories.models import Category


class ShowQuestion(ListView):
    model = Question
    template_name = 'questions/questions.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'questions'
    paginate_by = 1

    def get_queryset(self):
        print(Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category'))
        return Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')





# class ShowQuestion(DetailView):
#     model = Question
#     template_name = 'questions/questions.html'
#     pk_url_kwarg = 'pk'
#     context_object_name = 'question'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         all_questions = context['question'].category.questions.all()
#         gen_question = (i for i in range(len(all_questions)))
#         # for i in gen_question:
#         #         context['question'] = all_questions[i]
#         #         context['next_question'] = all_questions[i+1]
#         #         if i > 0:
#         #             context['previous_question'] = all_questions[i-1]
#         #         yield i
#         # for i in range(len(all_questions)):
#         #     print(i)
#         #     context['question'] = all_questions[i]
#         #     context['next_question'] = all_questions[i+1]
#         #     if i > 0:
#         #         context['previous_question'] = all_questions[i-1]
#         # context['other_questions_range'] = range(1, len(context['all_questions']))
#         # print(context['all_questions'][1], context['other_questions_range'])
#                 return context
#
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Question.objects, pk=self.kwargs[self.pk_url_kwarg])
