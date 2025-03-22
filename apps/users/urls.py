from django.urls import path
from users.views.users import (
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserDetailView,
    UserMessageView,
    UserExportCsvView,
    UserExportPDFView,
)
from users.views.groups import (
    GroupListView,
    GroupCreateView,
    GroupDetailView,
    GroupUpdateView,
    GroupDeleteView,
)

urlpatterns = [
    # CRUD de Usuários
    path("usuarios/", UserListView.as_view(), name="user-list"),
    path("usuarios/message/", UserMessageView.as_view(), name="user-message"),
    path("usuarios/inserir/", UserCreateView.as_view(), name="user-create"),
    path("usuarios/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("usuarios/<int:pk>/editar/", UserUpdateView.as_view(), name="user-update"),
    path("usuarios/<int:pk>/excluir/", UserDeleteView.as_view(), name="user-delete"),
    path("usuarios/exportcsv/", UserExportCsvView.as_view(), name="user-export-csv"),
    path("usuarios/exportpdf/", UserExportPDFView.as_view(), name="user-export-pdf"),
    # CRUD de Grupos
    path("grupos-usuarios/", GroupListView.as_view(), name="groups-list"),
    path("grupos-usuarios/inserir/", GroupCreateView.as_view(), name="groups-create"),
    path("grupos-usuarios/<int:pk>/", GroupDetailView.as_view(), name="groups-detail"),
    path(
        "grupos-usuarios/<int:pk>/editar/",
        GroupUpdateView.as_view(),
        name="groups-update",
    ),
    path(
        "grupos-usuarios/<int:pk>/excluir/",
        GroupDeleteView.as_view(),
        name="groups-delete",
    ),
]
