from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Suppliers
from .forms import SupplierForm


class SupplierListView(LoginRequiredMixin, ListView):
    model = Suppliers
    template_name = "suppliers/supplier_list.html"
    context_object_name = "suppliers"


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = "suppliers/supplier_form.html"
    success_url = reverse_lazy("supplier-list")


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = "suppliers/supplier_form.html"
    success_url = reverse_lazy("supplier-list")


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Suppliers
    template_name = "suppliers/supplier_confirm_delete.html"
    success_url = reverse_lazy("supplier-list")


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Suppliers
    template_name = "suppliers/supplier_detail.html"
    context_object_name = "supplier"
