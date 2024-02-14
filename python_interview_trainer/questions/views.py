from django.views.generic import ListView
from python_interview_trainer.questions.models import Question


class ShowQuestion(ListView):
    model = Question
    template_name = 'questions/questions.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'questions'
    paginate_by = 1

    def get_queryset(self):
        return Question.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')
