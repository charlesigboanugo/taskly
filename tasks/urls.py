from django.urls import path

from . import views


app_name = "tasks"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.createTask, name="createTask"),
    path("<int:task_id>/", views.singleTask, name="singleTask"),
    path("<int:task_id>/update/", views.updateTask, name="updateTask"),
    path("<int:task_id>/delete/", views.deleteTask, name="deleteTask"),
    path("<int:task_id>/complete/", views.completeTask, name="completeTask"),
    path("completed/", views.completedTasks, name="completedTasks"),
    path("scheduled/", views.scheduledTasks, name="scheduledTasks"),
    path("pending/", views.pendingTasks, name="pendingTasks"),
    path("running/", views.runningTasks, name="runningTasks"),
]