from utils import utils
from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_phone


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

    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20, validators=[validate_phone])
    oab = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)
    nacionalidade = models.CharField(max_length=255)
    estado_civil = models.CharField(max_length=255, choices=OPTIONS_ESTADO_CIVIL)
    seccional_oab = models.CharField(max_length=2, choices=OPTIONS_SECCTIONAL_OAB)

    def save(self, *args, **kwargs):
        self.telefone = utils.remove_special_characters(self.telefone)

        return super().save(*args, **kwargs)

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"
