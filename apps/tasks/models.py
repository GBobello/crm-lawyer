from django.db import models
from django.conf import settings


class Tasks(models.Model):
    STATUS_CHOICES = [
        ("agendada", "Agendada"),
        ("concluida", "Concluída"),
        ("cancelada", "Cancelada"),
    ]

    PRIORIDADE_CHOICES = [
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
    ]

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="usuario",
    )
    data = models.DateField(null=False, blank=False)
    hora = models.TimeField()
    hora_mensagem = models.TimeField()
    descricao = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Agendada")
    prioridade = models.CharField(max_length=5, choices=PRIORIDADE_CHOICES)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = "tasks"
        verbose_name = "Tarefa"
        verbose_name_plural = "Tarefas"
