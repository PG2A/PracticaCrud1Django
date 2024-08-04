from django.urls import path
from .views import list_task, create_tasks, delete_task

urlpatterns = [
    path('', list_task),
    path('new/', create_tasks, name='create_task'),
    path('delete_task/<int:id>/', delete_task, name='delete_task')
]