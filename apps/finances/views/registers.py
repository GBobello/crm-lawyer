from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import Registers
from finances.forms import RegisterForm


class RegisterListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Registers
    template_name = "registers/register_list.html"
    context_object_name = "register"
    permission_required = "finances.view_registers"


class RegisterCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Registers
    form_class = RegisterForm
    template_name = "registers/register_form.html"
    success_url = reverse_lazy("register-list")
    permission_required = "finances.add_registers"


class RegisterUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Registers
    form_class = RegisterForm
    template_name = "registers/register_form.html"
    success_url = reverse_lazy("register-list")
    permission_required = "finances.change_registers"


class RegisterDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Registers
    template_name = "registers/register_confirm_delete.html"
    success_url = reverse_lazy("register-list")
    permission_required = "finances.delete_registers"


class RegisterDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Registers
    template_name = "registers/register_detail.html"
    context_object_name = "Register"
    permission_required = "finances.view_registers"
