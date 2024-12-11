from django import forms
from .models import Tasks


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "data",
            "usuario",
            "hora",
            "hora_mensagem",
            "descricao",
            "status",
            "prioridade",
        ]

        widgets = {
            "data": forms.DateInput(attrs={"id": "data", "type": "date"}),
            "hora": forms.TimeInput(attrs={"type": "time"}),
            "hora_mensagem": forms.TimeInput(attrs={"type": "time"}),
        }
