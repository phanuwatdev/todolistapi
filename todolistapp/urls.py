from django.contrib import admin
from django.urls import path,include
from .api import router
from todolistapp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.api_list, name='api-list'),
    path('todo-list/', views.todo_list, name='todo-list/'),
    path('todo-create-task/', views.todo_create_task, name='todo-create-task'),
    path('todo-task-checked/<str:getid>', views.todo_task_checked, name='todo-task-checked'),
    # path('todo-update-task/<str:getid>', views.todo_update_task, name='todo-update-task'),
    path('todo-update-all/', views.todo_update_all, name='todo-update-all'),
    path('todo-delete-task/<str:getid>', views.todo_delete_task, name='todo-delete-task'),
    path('todo-delete-all/', views.todo_delete_all, name='todo-delete-all'),
]

urlpatterns = format_suffix_patterns(urlpatterns)