from django.urls import path
from . import views


urlpatterns = [
    path('', views.ShowQuestion.as_view(), name='show_question'),
    # path('<slug:cat_slug>/', views..as_view(), name='category'),
]
