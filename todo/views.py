from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem


def todo_view(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_todo_items': all_todo_items})


def add_todo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')


def delete_todo(request, todo_id):
    TodoItem.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')
