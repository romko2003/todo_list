from django.urls import path

from todo.views import (
    TagCreateView,
    TagDeleteView,
    TagListView,
    TagUpdateView,
    TaskCreateView,
    TaskDeleteView,
    TaskListView,
    TaskUpdateView,
    toggle_task_status,
)

app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),

    path("tasks/add/", TaskCreateView.as_view(), name="task-add"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/toggle/", toggle_task_status, name="task-toggle"),

    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagCreateView.as_view(), name="tag-add"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
