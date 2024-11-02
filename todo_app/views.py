from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import TaskForm
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "todo_app/task_list.html"

    def get_queryset(self):
        queryset = Task.objects.all()
        return queryset


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo_app:task-list")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo_app/tag_list.html"

    def get_queryset(self):
        queryset = Tag.objects.all()
        return queryset


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_app:tag-list")


class ToggleTaskStatusView(generic.View):
    @staticmethod
    def get(request, pk):
        task = Task.objects.get(id=pk)
        if task.is_done:
            task.is_done = False
        else:
            task.is_done = True
        task.save()

        return HttpResponseRedirect(
            reverse_lazy(
                "todo_app:task-list"
            )
        )
