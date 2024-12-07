from django.db import models


class Customer(models.Model):
    OPTIONS_TIPO_PESSOA = (
        ("fisica", "Física"),
        ("juridica", "Jurídica"),
    )

    OPTIONS_UF = (
        ("AC", "AC"),
        ("AL", "AL"),
        ("AP", "AP"),
        ("AM", "AM"),
        ("BA", "BA"),
        ("CE", "CE"),
        ("DF", "DF"),
        ("ES", "ES"),
        ("GO", "GO"),
        ("MA", "MA"),
        ("MT", "MT"),
        ("MS", "MS"),
        ("MG", "MG"),
        ("PA", "PA"),
        ("PB", "PB"),
        ("PR", "PR"),
        ("PE", "PE"),
        ("PI", "PI"),
        ("RJ", "RJ"),
        ("RN", "RN"),
        ("RS", "RS"),
        ("RO", "RO"),
        ("RR", "RR"),
        ("SC", "SC"),
        ("SP", "SP"),
        ("SE", "SE"),
        ("TO", "TO"),
    )

    OPTIONS_ESTADO_CIVIL = (
        ("solteiro", "Solteiro(a)"),
        ("casado", "Casado(a)"),
        ("divorciado", "Divorciado(a)"),
        ("viuvo", "Viúvo(a)"),
        ("separado judicialmente", "Separado(a) Judicialmente"),
        ("uniao estavel", "União Estável"),
    )

    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    data_cad = models.DateTimeField(auto_now_add=True)
    endereco = models.CharField(max_length=255, null=True, blank=True)
    cpf = models.CharField(max_length=14)
    tipo_pessoa = models.CharField(max_length=255, choices=OPTIONS_TIPO_PESSOA)
    data_nascimento = models.DateField(null=True, blank=True)
    numero = models.CharField(max_length=10, null=True, blank=True)
    bairro = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=OPTIONS_UF, null=True, blank=True)
    cep = models.CharField(max_length=9, null=True, blank=True)
    rg = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    genitor = models.CharField(max_length=255, null=True, blank=True)
    genitora = models.CharField(max_length=255, null=True, blank=True)
    profissao = models.CharField(max_length=255, null=True, blank=True)
    nacionalidade = models.CharField(max_length=255, null=True, blank=True)
    estado_civil = models.CharField(
        max_length=255, choices=OPTIONS_ESTADO_CIVIL, null=True, blank=True
    )

    class Meta:
        db_table = "customers"
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
