from django.contrib import admin
from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "telefone",
        "oab",
        "seccional_oab",
        "estado_civil",
    )
    search_fields = ("username", "email", "telefone", "oab")
    list_filter = ("seccional_oab", "estado_civil")
