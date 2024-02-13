from django.urls import path, include
from . import views


urlpatterns = [
    path('<slug:category_slug>', views.TestCategory.as_view(), name='category'),
    path('<slug:category_slug>/questions/', include('python_interview_trainer.questions.urls')),
    # path('<slug:cat_slug>/', views..as_view(), name='category'),
]
