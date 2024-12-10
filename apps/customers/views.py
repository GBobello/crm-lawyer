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


# Listagem dos clientes
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"


# Criação de um cliente
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    template_name = "customers/customer_form.html"
    fields = [
        "nome",
        "email",
        "telefone",
        "endereco",
        "cpf",
        "tipo_pessoa",
        "data_nascimento",
        "numero",
        "rg",
        "complemento",
        "genitor",
        "genitora",
        "profissao",
        "nacionalidade",
        "estado_civil",
    ]
    success_url = reverse_lazy("customer-list")


# Atualização de um cliente
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    template_name = "customers/customer_form.html"
    fields = [
        "nome",
        "email",
        "telefone",
        "endereco",
        "cpf",
        "tipo_pessoa",
        "data_nascimento",
        "numero",
        "rg",
        "complemento",
        "genitor",
        "genitora",
        "profissao",
        "nacionalidade",
        "estado_civil",
    ]
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
