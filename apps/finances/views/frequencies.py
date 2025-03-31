from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from finances.models import Frequencies
from finances.forms import FrequencyForm


class FrequencyListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Frequencies
    template_name = "frequencies/frequency_list.html"
    context_object_name = "frequency"
    permission_required = "finances.view_frequencies"


class FrequencyCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Frequencies
    form_class = FrequencyForm
    template_name = "frequencies/frequency_form.html"
    success_url = reverse_lazy("frequency-list")
    permission_required = "finances.add_frequencies"


class FrequencyUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Frequencies
    form_class = FrequencyForm
    template_name = "frequencies/frequency_form.html"
    success_url = reverse_lazy("frequency-list")
    permission_required = "finances.change_frequencies"


class FrequencyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Frequencies
    template_name = "frequencies/frequency_confirm_delete.html"
    success_url = reverse_lazy("frequency-list")
    permission_required = "finances.delete_frequencies"


class FrequencyDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Frequencies
    template_name = "frequencies/frequency_detail.html"
    context_object_name = "frequency"
    permission_required = "finances.view_frequencies"
