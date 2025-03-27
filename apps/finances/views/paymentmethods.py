from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import PaymentMethods
from finances.forms import PaymentMethodForm


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
