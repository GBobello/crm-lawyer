from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        exclude = ["usuario"]  # Usuário será atribuído automaticamente
