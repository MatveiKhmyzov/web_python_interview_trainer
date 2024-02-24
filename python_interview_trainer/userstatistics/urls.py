from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.AnswerView.as_view(), name='getting_answer'),
    # path('<slug:cat_slug>/', views..as_view(), name='category'),
]
