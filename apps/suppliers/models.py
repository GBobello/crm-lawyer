from django.db import models


class Supplier(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "suppliers"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
