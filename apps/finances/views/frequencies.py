from django.contrib.auth.mixins import LoginRequiredMixin
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
