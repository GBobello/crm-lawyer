from django.urls import path
from .views import (
    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,
    CustomerDetailView,
)

urlpatterns = [
    path("", CustomerListView.as_view(), name="customer-list"),
    path("inserir/", CustomerCreateView.as_view(), name="customer-create"),
    path("<int:pk>/", CustomerDetailView.as_view(), name="customer-detail"),
    path("<int:pk>/editar/", CustomerUpdateView.as_view(), name="customer-update"),
    path("<int:pk>/excluir/", CustomerDeleteView.as_view(), name="customer-delete"),
]
