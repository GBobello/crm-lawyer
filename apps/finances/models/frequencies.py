from django.db import models


class Frequencies(models.Model):
    frequency = models.CharField(max_length=255)
    days = models.IntegerField(default=0)

    def __str__(self):
        return self.frequency

    class Meta:
        db_table = "frequencies"
        verbose_name = "Frequência"
        verbose_name_plural = "Frequências"
