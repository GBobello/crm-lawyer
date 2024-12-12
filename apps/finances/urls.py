from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
    SupplierDetailView,
    PaymentMethodListView,
    PaymentMethodCreateView,
    PaymentMethodUpdateView,
    PaymentMethodDeleteView,
    PaymentMethodDetailView,
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
    path(
        "formas-pagamento/", PaymentMethodListView.as_view(), name="paymentmethod-list"
    ),
    path(
        "formas-pagamento/inserir/",
        PaymentMethodCreateView.as_view(),
        name="paymentmethod-create",
    ),
    path(
        "formas-pagamento/<int:pk>/",
        PaymentMethodDetailView.as_view(),
        name="paymentmethod-detail",
    ),
    path(
        "formas-pagamento/<int:pk>/editar/",
        PaymentMethodUpdateView.as_view(),
        name="paymentmethod-update",
    ),
    path(
        "formas-pagamento/<int:pk>/excluir/",
        PaymentMethodDeleteView.as_view(),
        name="paymentmethod-delete",
    ),
]
