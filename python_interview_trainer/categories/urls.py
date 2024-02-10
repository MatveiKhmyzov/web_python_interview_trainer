from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.TestCategory.as_view(), name='category_list'),
    path('questions/', include('python_interview_trainer.questions.urls')),
    # path('<slug:cat_slug>/', views..as_view(), name='category'),
]
