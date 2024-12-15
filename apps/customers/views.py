from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)
from .models import Customer
from .forms import CustomerForm
from django.db.models import Q
import csv
import datetime


class CustomerMessageView(LoginRequiredMixin, View):
    context_object_name = "message"

    def get(self, request, *args, **kwargs):
        # Aqui você pode definir a mensagem que deseja passar como resposta JSON
        response_data = {
            "message": "Operação concluída com sucesso!",
            "status": "success",
        }
        # Retorna a resposta JSON
        return JsonResponse(response_data)


class CustomerExportCsvView(LoginRequiredMixin, View):
    model = Customer
    context_object_name = "users"

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            "attachment; filename=Clientes" + str(datetime.datetime.now()) + ".csv"
        )

        writer = csv.writer(response)
        writer.writerow(
            [
                "Nome",
                "Email",
                "Telefone",
                "Documento",
                "Tipo Pessoa",
                "Data Nascimento",
                "Cidade",
                "Estado",
            ]
        )
        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"
        if search:
            Customers = Customer.objects.filter(
                Q(nome__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
                | Q(tipo_pessoa__icontains=search)
            ).order_by(orderby)
        else:
            Customers = Customer.objects.all().order_by(orderby)

        for customer in Customers:
            writer.writerow(
                [
                    customer.nome,
                    customer.email,
                    customer.telefone_formatado(),
                    customer.documento,
                    customer.get_tipo_pessoa_display(),
                    customer.data_nascimento,
                    customer.cidade,
                    customer.estado,
                ]
            )

        return response


# Listagem dos clientes
class CustomerListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Customer
    template_name = "customers/customer_list.html"
    context_object_name = "customers"

    def get_queryset(self):
        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"
        if search:
            return Customer.objects.filter(
                Q(nome__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
                | Q(tipo_pessoa__icontains=search)
            ).order_by(orderby)

        return Customer.objects.all().order_by(orderby)

    def get_template_names(self):
        content = self.request.META.get("CONTENT_TYPE")
        if content and "application/text" in content:
            return ["customers/customer_list_table.html"]
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = {
            "id": "Código 🔺",
            "nome": "Nome 🔺",
            "email": "E-mail 🔺",
            "telefone": "Telefone 🔺",
            "tipo_pessoa": "Tipo Pessoa 🔺",
            "data_cad": "Data de cadastro 🔺",
            "-id": "Código 🔻",
            "-nome": "Nome 🔻",
            "-email": "E-mail 🔻",
            "-telefone": "Telefone 🔻",
            "-tipo_pessoa": "Tipo Pessoa 🔻",
            "-data_cad": "Data de cadastro 🔻",
        }
        context["name_model"] = "Cliente"
        context["plural_name_model"] = "Clientes"

        return context


# Criação de um cliente
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer-message")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, "Cliente criado com sucesso!")
        # Retorna a resposta
        return response


# Atualização de um cliente
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_form.html"
    success_url = reverse_lazy("customer-message")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, "Cliente atualizado com sucesso!")
        # Retorna a resposta
        return response


# Exclusão de um cliente
class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("customer-message")


# Detalhes de um cliente
class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "customers/customer_detail.html"
    context_object_name = "customer"
