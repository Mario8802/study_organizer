from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task
from .forms import TaskForm, TaskEditForm


class TaskListView(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/task_create.html"
    success_url = reverse_lazy("task_list")

    def get_initial(self):
        initial = super().get_initial()
        course_id = self.request.GET.get("course")

        if course_id:
            initial["courses"] = [course_id]

        return initial

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskEditForm
    template_name = "tasks/task_edit.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "tasks/task_delete.html"
    success_url = reverse_lazy("task_list")


def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.completed = not task.completed
    task.save()

    return redirect(request.META.get("HTTP_REFERER"))
