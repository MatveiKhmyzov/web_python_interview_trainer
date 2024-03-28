from django.contrib import admin
from django.urls import path, include

from python_interview_trainer.userstatistics import views

urlpatterns = [
    path('<int:pk>', views.AnswerView.as_view(), name='getting_answer'),
    path('results', views.ResultView.as_view(), name='getting_result'),
    # path('<slug:cat_slug>/', views..as_view(), name='category'),
]
