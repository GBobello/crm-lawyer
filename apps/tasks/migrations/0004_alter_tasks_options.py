# Generated by Django 5.1.4 on 2024-12-18 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_usuario'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasks',
            options={'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]
