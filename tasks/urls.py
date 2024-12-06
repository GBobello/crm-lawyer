from django.urls import path
from .views import (
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("nova/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/editar/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/deletar/", TaskDeleteView.as_view(), name="task_delete"),
]
