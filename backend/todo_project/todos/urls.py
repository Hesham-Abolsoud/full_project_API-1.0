from django.urls import path
from todos.views import ListTodo, DetailTodo
#API url

urlpatterns = [
    path('<int:pk>/',DetailTodo.as_view()),
    path('',ListTodo.as_view()),
]

