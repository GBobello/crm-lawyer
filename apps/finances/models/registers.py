from django.db import models
from django.conf import settings


class Registers(models.Model):
    data_abertura = models.DateField(blank=False, null=False)
    data_fechamento = models.DateField(blank=True, null=True)
    valor_abertura = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_fechamento = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    usuario_abertura = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="usuario_abertura",
    )

    usuario_fechamento = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name="usuario_fechamento",
        blank=True,
        null=True,
    )
    obs = models.TextField(blank=True, null=True, verbose_name="Observações")

    class Meta:
        db_table = "registers"
        verbose_name = "Caixa"
        verbose_name_plural = "Caixas"
