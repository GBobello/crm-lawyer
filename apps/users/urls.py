from django.urls import path
from .views import (
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserDetailView,
    UserMessageView,
)

urlpatterns = [
    # CRUD de Usuários
    path("", UserListView.as_view(), name="user-list"),
    path("message/", UserMessageView.as_view(), name="user-message"),
    path("inserir/", UserCreateView.as_view(), name="user-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("<int:pk>/editar/", UserUpdateView.as_view(), name="user-update"),
    path("<int:pk>/excluir/", UserDeleteView.as_view(), name="user-delete"),
]
