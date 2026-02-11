from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from todo.forms import TagForm, TaskForm
from todo.models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "todo/tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return (
            Task.objects.prefetch_related("tags")
            .order_by("is_done", "-created_at")
        )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/tasks/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/tasks/task_form.html"
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/tasks/task_confirm_delete.html"
    success_url = reverse_lazy("todo:home")


def toggle_task_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save(update_fields=["is_done"])
    return redirect("todo:home")


class TagListView(ListView):
    model = Tag
    template_name = "todo/tags/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tags/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tags/tag_form.html"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/tags/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tag-list")
