from django.urls import reverse_lazy
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
class TaskListView(ListView):
    model = Tasks
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()  # Superusuário vê todas as tasks
        return Tasks.objects.filter(
            usuario=self.request.user
        )  # Usuários comuns só veem as suas


# Detalhes de uma Task
class TaskDetailView(DetailView):
    model = Tasks
    template_name = "tasks/task_detail.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        return Tasks.objects.filter(usuario=self.request.user)


# Criar Nova Task
class TaskCreateView(CreateView):
    model = Tasks
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.usuario = (
            self.request.user
        )  # Define o usuário atual como dono da task
        return super().form_valid(form)


# Editar Task
class TaskUpdateView(UpdateView):
    model = Tasks
    form_class = TaskForm
    template_name = "tasks/task_form.html"
    success_url = reverse_lazy("task_list")

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        return Tasks.objects.filter(usuario=self.request.user)


# Deletar Task
class TaskDeleteView(DeleteView):
    model = Tasks
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("task_list")

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Tasks.objects.all()
        return Tasks.objects.filter(usuario=self.request.user)
