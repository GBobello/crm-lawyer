from django.db import models


class ProvidedServices(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        db_table = "provided_services"
        verbose_name = "Serviço Prestado"
        verbose_name_plural = "Serviços Prestados"
