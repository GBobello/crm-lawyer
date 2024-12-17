from django.urls import path
from .views import (
    SupplierListView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,
    SupplierDetailView,
    SupplierMessageView,
    SupplierExportCsvView,
    SupplierExportPDFView,
    PaymentMethodListView,
    PaymentMethodCreateView,
    PaymentMethodUpdateView,
    PaymentMethodDeleteView,
    PaymentMethodDetailView,
    RegisterListView,
    RegisterCreateView,
    RegisterUpdateView,
    RegisterDeleteView,
    RegisterDetailView,
    FrequencyListView,
    FrequencyCreateView,
    FrequencyUpdateView,
    FrequencyDeleteView,
    FrequencyDetailView,
)

urlpatterns = [
    # suppliers
    path("fornecedores/", SupplierListView.as_view(), name="supplier-list"),
    path("message/", SupplierMessageView.as_view(), name="supplier-message"),
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
    path("exportcsv/", SupplierExportCsvView.as_view(), name="supplier-export-csv"),
    path("exportpdf/", SupplierExportPDFView.as_view(), name="supplier-export-pdf"),
    #  registers
    path("caixa/", RegisterListView.as_view(), name="register-list"),
    path("caixa/inserir/", RegisterCreateView.as_view(), name="register-create"),
    path("caixa/<int:pk>/", RegisterDetailView.as_view(), name="register-detail"),
    path(
        "caixa/<int:pk>/editar/",
        RegisterUpdateView.as_view(),
        name="register-update",
    ),
    path(
        "caixa/<int:pk>/excluir/",
        RegisterDeleteView.as_view(),
        name="register-delete",
    ),
    # payment methods
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
    # frequencies
    path("frequencias/", FrequencyListView.as_view(), name="frequency-list"),
    path(
        "frequencias/inserir/", FrequencyCreateView.as_view(), name="frequency-create"
    ),
    path(
        "frequencias/<int:pk>/", FrequencyDetailView.as_view(), name="frequency-detail"
    ),
    path(
        "frequencias/<int:pk>/editar/",
        FrequencyUpdateView.as_view(),
        name="frequency-update",
    ),
    path(
        "frequencias/<int:pk>/excluir/",
        FrequencyDeleteView.as_view(),
        name="frequency-delete",
    ),
]
