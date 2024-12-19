from utils import utils
from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_phone, validate_document
from utils import utils


class Users(AbstractUser):
    OPTIONS_SECCTIONAL_OAB = (
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

    OPTIONS_TIPO_PESSOA = (
        ("fisica", "Física"),
        ("juridica", "Jurídica"),
    )

    first_name = models.CharField(
        max_length=150, null=False, blank=False, verbose_name="Nome"
    )
    last_name = models.CharField(
        max_length=150, null=False, blank=True, verbose_name="Sobrenome"
    )
    endereco = models.CharField(max_length=255)
    documento = models.CharField(
        max_length=14, null=False, blank=False, validators=[validate_document]
    )
    tipo_pessoa = models.CharField(
        max_length=255, null=False, blank=False, choices=OPTIONS_TIPO_PESSOA
    )
    telefone = models.CharField(max_length=20, validators=[validate_phone])
    oab = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)
    nacionalidade = models.CharField(max_length=255)
    estado_civil = models.CharField(max_length=255, choices=OPTIONS_ESTADO_CIVIL)
    seccional_oab = models.CharField(max_length=2, choices=OPTIONS_SECCTIONAL_OAB)

    def telefone_formatado(self):
        return utils.telefone_formatado(self.telefone)

    def save(self, *args, **kwargs):
        print(self.foto)
        self.documento = utils.remove_special_characters(self.documento)
        self.telefone = utils.remove_special_characters(self.telefone)

        if len(self.documento) == 11:
            self.tipo_pessoa = "fisica"
        else:
            self.tipo_pessoa = "juridica"

        return super().save(*args, **kwargs)

    class Meta:
        db_table = "users"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
