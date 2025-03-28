# Generated by Django 5.1.4 on 2024-12-19 16:17

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models
from apps.utils import utils


def create_default_user(apps, schema_editor):
    users = apps.get_model("users", "Users")

    first_name = "admin"
    documento = "07168369989"
    tipo_pessoa = "fisica"
    username = "admin"
    email = "contato@email.com"
    password = "admin"
    endereco = "Rua dos Advogados, 123"
    telefone = "11 99999-9999"
    oab = "123456"
    especialidade = "Direito Civil"
    nacionalidade = "Brasileiro"
    estado_civil = "Solteiro"
    seccional_oab = "SC"

    if not users.objects.filter(username=username).exists():
        users.objects.create_superuser(
            first_name=first_name,
            documento=documento,
            tipo_pessoa=tipo_pessoa,
            username=username,
            email=email,
            password=password,
            endereco=endereco,
            telefone=telefone,
            oab=oab,
            especialidade=especialidade,
            nacionalidade=nacionalidade,
            estado_civil=estado_civil,
            seccional_oab=seccional_oab,
        )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Users",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("first_name", models.CharField(max_length=150)),
                ("last_name", models.CharField(blank=True, max_length=150)),
                ("endereco", models.CharField(max_length=255)),
                (
                    "documento",
                    models.CharField(
                        max_length=14, validators=[utils.validate_document]
                    ),
                ),
                (
                    "tipo_pessoa",
                    models.CharField(
                        choices=[("fisica", "Física"), ("juridica", "Jurídica")],
                        max_length=255,
                    ),
                ),
                (
                    "telefone",
                    models.CharField(max_length=20, validators=[utils.validate_phone]),
                ),
                ("oab", models.CharField(max_length=20)),
                ("especialidade", models.CharField(max_length=255)),
                ("foto", models.ImageField(blank=True, null=True, upload_to="fotos/")),
                ("nacionalidade", models.CharField(max_length=255)),
                (
                    "estado_civil",
                    models.CharField(
                        choices=[
                            ("solteiro", "Solteiro(a)"),
                            ("casado", "Casado(a)"),
                            ("divorciado", "Divorciado(a)"),
                            ("viuvo", "Viúvo(a)"),
                            ("separado judicialmente", "Separado(a) Judicialmente"),
                            ("uniao estavel", "União Estável"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "seccional_oab",
                    models.CharField(
                        choices=[
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
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Usuário",
                "verbose_name_plural": "Usuários",
                "db_table": "users",
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RunPython(create_default_user),
    ]
