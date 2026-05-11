from django.urls import path
from .views import todo_list_create, todo_detail

urlpatterns = [
    path('todos/', todo_list_create, name='list_create_todo'),
    path('todos/<int:pk>/', todo_detail, name='todo_detail'),

]
