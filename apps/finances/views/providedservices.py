from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import ProvidedServices
from finances.forms import ProvidedServicesForm


class ProvidedServicesListView(LoginRequiredMixin, ListView):
    model = ProvidedServices
    template_name = "providedservices/providedservices_list.html"
    context_object_name = "providedservices"


class ProvidedServicesCreateView(LoginRequiredMixin, CreateView):
    model = ProvidedServices
    form_class = ProvidedServicesForm
    template_name = "providedservices/providedservices_form.html"
    success_url = reverse_lazy("providedservices-list")


class ProvidedServicesUpdateView(LoginRequiredMixin, UpdateView):
    model = ProvidedServices
    form_class = ProvidedServicesForm
    template_name = "providedservices/providedservices_form.html"
    success_url = reverse_lazy("providedservices-list")


class ProvidedServicesDeleteView(LoginRequiredMixin, DeleteView):
    model = ProvidedServices
    template_name = "providedservices/providedservices_confirm_delete.html"
    success_url = reverse_lazy("providedservices-list")


class ProvidedServicesDetailView(LoginRequiredMixin, DetailView):
    model = ProvidedServices
    template_name = "providedservices/providedservices_detail.html"
    context_object_name = "providedservices"
