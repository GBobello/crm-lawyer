from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import Payable
from finances.forms import PayableForm


class PayableListView(LoginRequiredMixin, ListView):
    model = Payable
    template_name = "payable/payable_list.html"
    context_object_name = "payable"


class PayableCreateView(LoginRequiredMixin, CreateView):
    model = Payable
    form_class = PayableForm
    template_name = "payable/payable_form.html"
    success_url = reverse_lazy("payable-list")


class PayableUpdateView(LoginRequiredMixin, UpdateView):
    model = Payable
    form_class = PayableForm
    template_name = "payable/payable_form.html"
    success_url = reverse_lazy("payable-list")


class PayableDeleteView(LoginRequiredMixin, DeleteView):
    model = Payable
    template_name = "payable/payable_confirm_delete.html"
    success_url = reverse_lazy("payable-list")


class PayableDetailView(LoginRequiredMixin, DetailView):
    model = Payable
    template_name = "payable/payable_detail.html"
    context_object_name = "payable"
