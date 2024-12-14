# Generated by Django 5.1.4 on 2024-12-14 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_alter_paymentmethods_options_alter_registers_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frequencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.CharField(max_length=255)),
                ('days', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Frequency',
                'verbose_name_plural': 'Frequencies',
                'db_table': 'frequencies',
            },
        ),
        migrations.AlterModelTable(
            name='registers',
            table='registers',
        ),
    ]
