from django.contrib import admin
from django.urls import path, include
from python_interview_trainer.interview import views


urlpatterns = [
    path('', views.index),
    path('cats/', views.categories),
]
