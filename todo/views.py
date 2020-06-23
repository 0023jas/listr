from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
from .models import CurrentlyWorkingItem
from .models import FinishedItem
#from django.views.decorators.csrf import ensure_csrf_cookie
#@ensure_csrf_cookie

# Create your views here.
def todoView(request):
    all_todo_items = TodoItem.objects.filter(userName = request.user.username)
    all_currentlyWorking_items = CurrentlyWorkingItem.objects.filter(userName = request.user.username)
    all_finished_items = FinishedItem.objects.filter(userName = request.user.username)
    return render(request, "home.html",
        {'all_items': all_todo_items,
        'all_CW_items': all_currentlyWorking_items,
        'all_f_items': all_finished_items
        })
    
def addTodo(request):
    new_item = TodoItem(content = request.POST['content'], userName = request.user.username)
    new_item.save()
    return HttpResponseRedirect('/')

def deleteTodo(request, todo_id):
    item_to_delete = TodoItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')

def deleteTodoFinal(request, todo_id):
    item_to_delete = FinishedItem.objects.get(id=todo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/')

def moveTodo(request, todo_id):
    item_to_move = TodoItem.objects.get(id=todo_id)
    new_item_to_move = item_to_move.content
    new_item = CurrentlyWorkingItem(contentCW = new_item_to_move, userName = request.user.username)
    new_item.save()
    item_to_move.delete()
    return HttpResponseRedirect('/')

def finishTodo(request, todo_id):
    item_to_finalize = CurrentlyWorkingItem.objects.get(id=todo_id)
    new_item_to_finalize = item_to_finalize.contentCW
    new_item = FinishedItem(contentDone = new_item_to_finalize, userName = request.user.username)
    new_item.save()
    item_to_finalize.delete()
    return HttpResponseRedirect('/')