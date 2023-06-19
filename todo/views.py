from django.shortcuts import render, redirect
from .models import Task

def todo_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Task.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    task.delete()
    return redirect('todo_list')

def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        title = request.POST['title']
        task.title = title
        task.save()
        return redirect('todo_list')
    return render(request, 'todo/edit_task.html', {'task': task})
