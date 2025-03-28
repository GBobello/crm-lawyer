# Generated by Django 5.1.4 on 2025-03-26 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0008_providedservices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('payment_date', models.DateField(blank=True, default=None, null=True)),
                ('obs', models.TextField()),
                ('frequency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.frequencies')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.paymentmethods')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.suppliers')),
            ],
            options={
                'verbose_name': 'Contas a pagar',
                'verbose_name_plural': 'Contas a pagar',
                'db_table': 'payable',
            },
        ),
    ]
