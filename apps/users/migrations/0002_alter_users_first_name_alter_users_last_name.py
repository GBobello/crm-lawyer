# Generated by Django 5.1.4 on 2024-12-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='first_name',
            field=models.CharField(max_length=150, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='users',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='Sobrenome'),
        ),
    ]
