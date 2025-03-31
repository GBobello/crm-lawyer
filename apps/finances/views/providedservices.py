from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import ProvidedServices
from finances.forms import ProvidedServicesForm


class ProvidedServicesListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = ProvidedServices
    template_name = "providedservices/providedservices_list.html"
    context_object_name = "providedservices"
    permission_required = "finances.view_providedservices"


class ProvidedServicesCreateView(
    LoginRequiredMixin, PermissionRequiredMixin, CreateView
):
    model = ProvidedServices
    form_class = ProvidedServicesForm
    template_name = "providedservices/providedservices_form.html"
    success_url = reverse_lazy("providedservices-list")
    permission_required = "finances.add_providedservices"


class ProvidedServicesUpdateView(
    LoginRequiredMixin, PermissionRequiredMixin, UpdateView
):
    model = ProvidedServices
    form_class = ProvidedServicesForm
    template_name = "providedservices/providedservices_form.html"
    success_url = reverse_lazy("providedservices-list")
    permission_required = "finances.change_providedservices"


class ProvidedServicesDeleteView(
    LoginRequiredMixin, PermissionRequiredMixin, DeleteView
):
    model = ProvidedServices
    template_name = "providedservices/providedservices_confirm_delete.html"
    success_url = reverse_lazy("providedservices-list")
    permission_required = "finances.delete_providedservices"


class ProvidedServicesDetailView(
    LoginRequiredMixin, PermissionRequiredMixin, DetailView
):
    model = ProvidedServices
    template_name = "providedservices/providedservices_detail.html"
    context_object_name = "providedservices"
    permission_required = "finances.view_providedservices"
