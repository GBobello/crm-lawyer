from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    oab = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=255)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)
    nacionalidade = models.CharField(max_length=255)
    estado_civil = models.CharField(max_length=255)
    seccional_oab = models.CharField(max_length=255)
