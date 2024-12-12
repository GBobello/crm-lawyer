# Generated by Django 5.1.4 on 2024-12-12 00:44

import finances.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_suppliers_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('taxa', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
            options={
                'verbose_name': 'Forma de Pagamento',
                'verbose_name_plural': 'Formas de Pagamento',
                'db_table': 'formas_pgto',
            },
        ),
        migrations.AlterField(
            model_name='suppliers',
            name='documento',
            field=models.CharField(max_length=18, validators=[finances.validators.validate_document]),
        ),
    ]