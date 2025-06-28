from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from datetime import date, timedelta
from django.contrib import messages

from .models import Task

# Create your views here.
@login_required
def index(request):
    user_id = request.user.pk
    now = date.today()
    tasks_list = Task.objects.filter(user_id=user_id)
    return render(request, "tasks/index.html", {"tasks_list": tasks_list, "now": now})

@login_required
def createTask(request):
    if request.method == "POST":
        user = request.user
        allowed_fields = ['title', 'description', 'start_at', 'due_at' ]  # only fields you want to update
        update_data = {key: request.POST[key] for key in allowed_fields if key in request.POST}
        task = Task.objects.create(user_id=user, **update_data)
        print(task)
        return redirect(f'/tasks/{task.pk}')
    else:
        now = date.today()
        now_plus_1_day = date.today() + timedelta(days=1)
        context = {
            "min_1_day": now_plus_1_day,
            "now": now,
        }
        return render(request, "tasks/create.html", context)

@login_required
def singleTask(request, task_id):
    now = date.today()
    user_id = request.user.pk
    task = get_object_or_404(Task, pk=task_id, user_id=user_id)
    return render (request, "tasks/single.html", {"task": task, "now": now})
   
@login_required
def updateTask(request, task_id):
    now = date.today()
    user_id = request.user.pk
    task = get_object_or_404(Task, pk=task_id, user_id=user_id)
    if request.method == "POST":
        allowed_fields = ['title', 'description', ]  # only fields you want to update
        if task.due_at <= now:
            allowed_fields.append("due_at")
        if task.start_at > now:
            allowed_fields.append("start_at")
        update_data = {key: request.POST[key] for key in allowed_fields if key in request.POST}
        Task.objects.filter(pk=task_id).update(**update_data)
        return redirect(f'/tasks/{task_id}')
    else:
        now_plus_1_day = date.today() + timedelta(days=1)
        context = {
            "task": task,
            "min_1_day": now_plus_1_day,
            "now": now,
        }
        return render(request, "tasks/update.html", context)

@login_required
def deleteTask(request, task_id):
    if request.method == "GET":
        raise Http404("not found")
    else:
        Task.objects.filter(pk=task_id).delete()
        return redirect('tasks:index')

@login_required
def completeTask(request, task_id):
    if request.method == "GET":
        raise Http404("not found")
    else:
        Task.objects.filter(pk=task_id).update(is_completed=True)
        messages.success(request, "Task created successfully!")
        return redirect('tasks:singleTask', task_id)
    
@login_required
def completedTasks(request):
    now = date.today()
    user_id = request.user.pk
    completed = Task.objects.filter(user_id=user_id, is_completed=True)
    return render(request, "tasks/index.html", {"tasks_list": completed, "now": now})

@login_required
def pendingTasks(request):
    now = date.today()
    user_id = request.user.pk
    now = date.today()
    pending = Task.objects.filter(user_id=user_id, due_at__lte=now, is_completed=False)
    return render(request, "tasks/index.html", {"tasks_list": pending, "now": now})

@login_required
def runningTasks(request):
    now = date.today()
    user_id = request.user.pk
    now = date.today()
    pending = Task.objects.filter(user_id=user_id, due_at__gt=now, start_at__lte=now, is_completed=False)
    return render(request, "tasks/index.html", {"tasks_list": pending, "now": now})

@login_required
def scheduledTasks(request):
    now = date.today()
    user_id = request.user.pk
    now = date.today()
    scheduled = Task.objects.filter(user_id=user_id, due_at__gt=now, start_at__gt=now, is_completed=False)
    return render(request, "tasks/index.html", {"tasks_list": scheduled, "now": now})
