from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
    SupplierDetailView,
)

urlpatterns = [
    path("fornecedores/", SupplierListView.as_view(), name="supplier-list"),
    path("fornecedores/inserir/", SupplierCreateView.as_view(), name="supplier-create"),
    path(
        "fornecedores/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"
    ),
    path(
        "fornecedores/<int:pk>/editar/",
        SupplierUpdateView.as_view(),
        name="supplier-update",
    ),
    path(
        "fornecedores/<int:pk>/excluir/",
        SupplierDeleteView.as_view(),
        name="supplier-delete",
    ),
]
