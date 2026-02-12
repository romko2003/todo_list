from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from todo.forms import TagForm, TaskForm
from todo.models import Tag, Task


class TaskListView(ListView):
    model = Task
    template_name = "todo/tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.prefetch_related("tags").order_by("is_done", "-created_at")


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


class TaskToggleStatusView(View):
    """
    Toggles task status: done <-> not done.
    POST-only (used by the Complete/Undo form button).
    Redirects back to the home page.
    """

    def post(self, request, pk: int, *args, **kwargs) -> HttpResponse:
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save(update_fields=["is_done"])
        # Using reverse_lazy keeps it consistent with CBV style
        return HttpResponse(status=302, headers={"Location": reverse_lazy("todo:home")})


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
