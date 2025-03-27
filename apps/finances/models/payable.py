from django.db import models
from finances.models import Suppliers


class Payable(models.Model):
    description = models.CharField(max_length=255, blank=False, null=False)
    value = models.DecimalField(
        max_digits=10, decimal_places=2, blank=False, null=False
    )
    supplier = models.ForeignKey(
        Suppliers, on_delete=models.CASCADE, blank=False, null=False
    )
    due_date = models.DateField(blank=False, null=False)
    payment_date = models.DateField(default=None, blank=True, null=True)
    payment_method = models.ForeignKey(
        "finances.PaymentMethods", on_delete=models.CASCADE, blank=False, null=False
    )
    frequency = models.ForeignKey("finances.Frequencies", on_delete=models.CASCADE)
    obs = models.TextField()

    def __str__(self):
        return self.description

    class Meta:
        db_table = "payable"
        verbose_name = "Contas a pagar"
        verbose_name_plural = "Contas a pagar"
