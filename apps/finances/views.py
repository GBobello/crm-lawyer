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

from apps.utils import utils
from .models import Suppliers, PaymentMethods, Registers, Frequencies
from .forms import SupplierForm, PaymentMethodForm, RegisterForm, FrequencyForm
from django.db.models import Q
import csv
import datetime

# Importações adicionais para gerar PDFs
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.utils import timezone
import textwrap



class SupplierMessageView(LoginRequiredMixin, View):
    context_object_name = "message"

    def get(self, request, *args, **kwargs):
        # Aqui você pode definir a mensagem que deseja passar como resposta JSON
        response_data = {
            "message": "Operação concluída com sucesso!",
            "status": "success",
        }
        # Retorna a resposta JSON
        return JsonResponse(response_data)


class SupplierExportCsvView(LoginRequiredMixin, View):
    model = Suppliers
    context_object_name = "users"

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            "attachment; filename=Fornecedores" + str(datetime.datetime.now()) + ".csv"
        )

        writer = csv.writer(response)
        writer.writerow(
            [
                "Nome",
                "Email",
                "Telefone",
                "Documento",
                "Tipo Pessoa",
                "Data Cadastro",
                "Endereço",
            ]
        )
        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"
        if search:
            Suppliers2 = Suppliers.objects.filter(
                Q(nome__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
                | Q(tipo_pessoa__icontains=search)
            ).order_by(orderby)
        else:
            Suppliers2 = Suppliers.objects.all().order_by(orderby)

        for supplier in Suppliers2:
            writer.writerow(
                [
                    supplier.nome,
                    supplier.email,
                    supplier.telefone_formatado(),
                    supplier.documento,
                    supplier.get_tipo_pessoa_display(),
                    utils.get_data_formatada(supplier.data_cadastro),
                    supplier.endereco,
                ]
            )

        return response


class SupplierListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Suppliers
    template_name = "suppliers/supplier_list.html"
    context_object_name = "suppliers"

    def get_queryset(self):
        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"

        if search:
            return self.model.objects.filter(
                Q(nome__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
                | Q(tipo_pessoa__icontains=search)
            ).order_by(orderby)

        return Suppliers.objects.all().order_by(orderby)

    def get_template_names(self):
        content = self.request.META.get("CONTENT_TYPE")
        if content and "application/text" in content:
            return ["suppliers/supplier_list_table.html"]
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields"] = {
            "id": "Código ",
            "nome": "Nome ",
            "email": "E-mail ",
            "telefone": "Telefone ",
            "tipo_pessoa": "Tipo Pessoa ",
            "data_cadastro": "Data de cadastro ",
        }
        context["name_model"] = "Fornecedor"
        context["plural_name_model"] = "Fornecedores"

        return context


class SupplierExportPDFView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=Clientes_{timezone.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf'

        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        p.setFont("Helvetica-Bold", 16)
        p.drawString(30, height - 50, "Relatório de Fornecedores")

        headers = [
            "Nome",
            "Email",
            "Telefone",
            "Documento",
            "Tipo",
            "Data Cad.",
            "Endereço",
        ]

        p.setFont("Helvetica-Bold", 8)
        x_offsets = [30, 120, 200, 270, 340, 380, 440]
        y = height - 80
        for i, header in enumerate(headers):
            p.drawString(x_offsets[i], y, header)

        # Linha horizontal
        p.line(30, y - 5, width - 30, y - 5)

        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"
        if search:
            Suppliers2 = Suppliers.objects.filter(
                Q(nome__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
                | Q(tipo_pessoa__icontains=search)
            ).order_by(orderby)
        else:
            Suppliers2 = Suppliers.objects.all().order_by(orderby)

        p.setFont("Helvetica", 8)
        y = height - 100
        line_height = 14


        for supplier in Suppliers2:
            texts = [
                    supplier.nome,
                    supplier.email,
                    supplier.telefone_formatado(),
                    supplier.documento,
                    supplier.get_tipo_pessoa_display(),
                    utils.get_data_formatada(supplier.data_cadastro),
                    supplier.endereco,
             ]


            max_lines = 1
            for i, text in enumerate(texts):
                wrapped_text = p.beginText(x_offsets[i], y)
                lines = textwrap.wrap(text, width=15)
                max_lines = max(max_lines, len(lines))
                for line in lines:
                    wrapped_text.textLine(line)
                p.drawText(wrapped_text)

            y -= max_lines * line_height

            if y < 50:
                p.showPage()
                y = height - 50

                p.setFont("Helvetica-Bold", 12)
                for i, header in enumerate(headers):
                    p.drawString(x_offsets[i], y, header)
                p.line(30, y - 5, width - 30, y - 5)
                p.setFont("Helvetica", 10)
                y = height - 100

        p.showPage()
        p.save()

        return response


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = "suppliers/supplier_form.html"
    success_url = reverse_lazy("supplier-message")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, "Fornecedor criado com sucesso!")
        # Retorna a resposta
        return response


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Suppliers
    form_class = SupplierForm
    template_name = "suppliers/supplier_form.html"
    success_url = reverse_lazy("supplier-message")

    def form_valid(self, form):
        response = super().form_valid(form)
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, "Fornecedor atualizado com sucesso!")
        # Retorna a resposta
        return response


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Suppliers
    template_name = "suppliers/supplier_confirm_delete.html"
    success_url = reverse_lazy("supplier-list")


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Suppliers
    template_name = "suppliers/supplier_detail.html"
    context_object_name = "supplier"


class PaymentMethodListView(LoginRequiredMixin, ListView):
    model = PaymentMethods
    template_name = "paymentmethods/paymentmethod_list.html"
    context_object_name = "paymentmethod"


class PaymentMethodCreateView(LoginRequiredMixin, CreateView):
    model = PaymentMethods
    form_class = PaymentMethodForm
    template_name = "paymentmethods/paymentmethod_form.html"
    success_url = reverse_lazy("paymentmethod-list")


class PaymentMethodUpdateView(LoginRequiredMixin, UpdateView):
    model = PaymentMethods
    form_class = PaymentMethodForm
    template_name = "paymentmethods/paymentmethod_form.html"
    success_url = reverse_lazy("paymentmethod-list")


class PaymentMethodDeleteView(LoginRequiredMixin, DeleteView):
    model = PaymentMethods
    template_name = "paymentmethods/paymentmethod_confirm_delete.html"
    success_url = reverse_lazy("paymentmethod-list")


class PaymentMethodDetailView(LoginRequiredMixin, DetailView):
    model = PaymentMethods
    template_name = "paymentmethods/paymentmethod_detail.html"
    context_object_name = "paymentmethod"


class RegisterListView(LoginRequiredMixin, ListView):
    model = Registers
    template_name = "registers/register_list.html"
    context_object_name = "register"


class RegisterCreateView(LoginRequiredMixin, CreateView):
    model = Registers
    form_class = RegisterForm
    template_name = "registers/register_form.html"
    success_url = reverse_lazy("register-list")


class RegisterUpdateView(LoginRequiredMixin, UpdateView):
    model = Registers
    form_class = RegisterForm
    template_name = "registers/register_form.html"
    success_url = reverse_lazy("register-list")


class RegisterDeleteView(LoginRequiredMixin, DeleteView):
    model = Registers
    template_name = "registers/register_confirm_delete.html"
    success_url = reverse_lazy("register-list")


class RegisterDetailView(LoginRequiredMixin, DetailView):
    model = Registers
    template_name = "registers/register_detail.html"
    context_object_name = "Register"


class FrequencyListView(LoginRequiredMixin, ListView):
    model = Frequencies
    template_name = "frequencies/frequency_list.html"
    context_object_name = "frequency"


class FrequencyCreateView(LoginRequiredMixin, CreateView):
    model = Frequencies
    form_class = FrequencyForm
    template_name = "frequencies/frequency_form.html"
    success_url = reverse_lazy("frequency-list")


class FrequencyUpdateView(LoginRequiredMixin, UpdateView):
    model = Frequencies
    form_class = FrequencyForm
    template_name = "frequencies/frequency_form.html"
    success_url = reverse_lazy("frequency-list")


class FrequencyDeleteView(LoginRequiredMixin, DeleteView):
    model = Frequencies
    template_name = "frequencies/frequency_confirm_delete.html"
    success_url = reverse_lazy("frequency-list")


class FrequencyDetailView(LoginRequiredMixin, DetailView):
    model = Frequencies
    template_name = "frequencies/frequency_detail.html"
    context_object_name = "frequency"
