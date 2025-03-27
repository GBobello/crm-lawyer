from django.db import models


class PaymentMethods(models.Model):
    nome = models.CharField(max_length=255)
    taxa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = "payment_methods"
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamento"
