from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
    SupplierDetailView,
)

urlpatterns = [
    path("", SupplierListView.as_view(), name="supplier-list"),
    path("inserir/", SupplierCreateView.as_view(), name="supplier-create"),
    path("<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("<int:pk>/editar/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("<int:pk>/excluir/", SupplierDeleteView.as_view(), name="supplier-delete"),
]
