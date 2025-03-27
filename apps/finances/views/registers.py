from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import Registers
from finances.forms import RegisterForm


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
