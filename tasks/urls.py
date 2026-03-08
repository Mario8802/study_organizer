from django.urls import path
from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView, toggle_task

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("edit/<int:pk>", TaskUpdateView.as_view(), name="task_edit"),
    path("delete/<int:pk>", TaskDeleteView.as_view(), name="task_delete"),
    path("toggle/<int:pk>/", toggle_task, name="task_toggle"),
]
