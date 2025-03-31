from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import PaymentMethods
from finances.forms import PaymentMethodForm


class PaymentMethodListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = PaymentMethods
    template_name = "paymentmethods/paymentmethod_list.html"
    context_object_name = "paymentmethod"
    permission_required = "finances.view_paymentmethods"


class PaymentMethodCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = PaymentMethods
    form_class = PaymentMethodForm
    template_name = "paymentmethods/paymentmethod_form.html"
    success_url = reverse_lazy("paymentmethod-list")
    permission_required = "finances.add_paymentmethods"


class PaymentMethodUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = PaymentMethods
    form_class = PaymentMethodForm
    template_name = "paymentmethods/paymentmethod_form.html"
    success_url = reverse_lazy("paymentmethod-list")
    permission_required = "finances.change_paymentmethods"


class PaymentMethodDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = PaymentMethods
    template_name = "paymentmethods/paymentmethod_confirm_delete.html"
    success_url = reverse_lazy("paymentmethod-list")
    permission_required = "finances.delete_paymentmethods"


class PaymentMethodDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = PaymentMethods
    template_name = "paymentmethods/paymentmethod_detail.html"
    context_object_name = "paymentmethod"
    permission_required = "finances.view_paymentmethods"
