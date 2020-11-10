from django.urls import path
from . import views

urlpatterns = [
    path('', views.todosTask, name='tasks'),
    path('add_task', views.todosAddTask, name='add_task'),
    path('update_task/<str:pk>/', views.todosUpdateTask, name="update_task"),
    path('delete/<str:pk>/', views.todosDeleteTask, name="delete"),
]