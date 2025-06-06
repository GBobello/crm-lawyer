from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .forms import TaskForm
from .models import Tasks


# Listar Tasks
class TaskListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Tasks
    template_name = "tasks/task_list.html"
    permission_required = "tasks.view_tasks"
    context_object_name = "tasks"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()  # Superusuário vê todas as tasks
        return Tasks.objects.filter(
            usuario=self.request.user
        )  # Usuários comuns só veem as suas


# Detalhes de uma Task
class TaskDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Tasks
    template_name = "tasks/task_detail.html"
    permission_required = "tasks.view_tasks"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        return Tasks.objects.filter(usuario=self.request.user)


# Criar Nova Task
class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    permission_required = "tasks.add_tasks"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            form.instance.usuario = self.request.user
        return super().form_valid(form)


# Editar Task
class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    permission_required = "tasks.change_tasks"
    success_url = reverse_lazy("task-list")

    def form_valid(self, form):
        if not self.request.user.is_superuser:
            form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        return Tasks.objects.filter(usuario=self.request.user)


# Deletar Task
class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Tasks
    template_name = "tasks/task_confirm_delete.html"
    permission_required = "tasks.delete_tasks"
    success_url = reverse_lazy("task-list")

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        return Tasks.objects.filter(usuario=self.request.user)
