from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import Payable
from finances.forms import PayableForm


class PayableListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Payable
    template_name = "payable/payable_list.html"
    context_object_name = "payable"
    permission_required = "finances.view_payable"


class PayableCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Payable
    form_class = PayableForm
    template_name = "payable/payable_form.html"
    success_url = reverse_lazy("payable-list")
    permission_required = "finances.add_payable"


class PayableUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Payable
    form_class = PayableForm
    template_name = "payable/payable_form.html"
    success_url = reverse_lazy("payable-list")
    permission_required = "finances.change_payable"


class PayableDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Payable
    template_name = "payable/payable_confirm_delete.html"
    success_url = reverse_lazy("payable-list")
    permission_required = "finances.delete_payable"


class PayableDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Payable
    template_name = "payable/payable_detail.html"
    context_object_name = "payable"
    permission_required = "finances.view_payable"
