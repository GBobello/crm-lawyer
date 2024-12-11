from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Customer
from .forms import CustomerForm


# Listagem dos clientes
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"


# Criação de um cliente
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer-list")


# Atualização de um cliente
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer-list")


# Exclusão de um cliente
class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customer-list")


# Detalhes de um cliente
class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "customer"
