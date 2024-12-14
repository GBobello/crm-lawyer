from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from .models import Suppliers, PaymentMethods, Registers, Frequencies
from .forms import SupplierForm, PaymentMethodForm, RegisterForm, FrequencyForm


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
