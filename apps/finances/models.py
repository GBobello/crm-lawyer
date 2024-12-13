from django.db import models
from django.conf import settings
from utils import utils
from .validators import validate_document, validate_phone


class Suppliers(models.Model):
    OPTIONS_TIPO_PESSOA = (
        ("fisica", "Física"),
        ("juridica", "Jurídica"),
    )

    nome = models.CharField(max_length=100)
    documento = models.CharField(max_length=18, validators=[validate_document])
    tipo_pessoa = models.CharField(max_length=255, choices=OPTIONS_TIPO_PESSOA)
    telefone = models.CharField(
        max_length=20, null=True, blank=True, validators=[validate_phone]
    )
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.documento = utils.remove_special_characters(self.documento)
        self.telefone = utils.remove_special_characters(self.telefone)

        if len(self.documento) == 11:
            self.tipo_pessoa = "fisica"
        else:
            self.tipo_pessoa = "juridica"

        return super().save(*args, **kwargs)

    class Meta:
        db_table = "suppliers"
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"


class PaymentMethods(models.Model):
    nome = models.CharField(max_length=255)
    taxa = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    class Meta:
        db_table = "formas_pgto"
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamento"


class Registers(models.Model):
    data_abertura = models.DateField(blank=False, null=False)
    data_fechamento = models.DateField(blank=True, null=True)
    valor_abertura = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    valor_fechamento = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )
    usuario_abertura = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="usuario_abertura",
    )

    usuario_fechamento = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="usuario_fechamento",
        blank=True,
        null=True,
    )
    obs = models.TextField(blank=True, null=True, verbose_name="Observações")
