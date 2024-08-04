from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def list_task(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'list_task.html', { "tasks": tasks })

def create_tasks(request):
    task = Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    print(request.POST)
    return redirect('/tasks/')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    print('id', id)
    return redirect('/tasks/')