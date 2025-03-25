from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task-detail"),
    path("inserir/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/editar/", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/excluir/", TaskDeleteView.as_view(), name="task-delete"),
]
