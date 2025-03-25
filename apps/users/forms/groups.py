from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import gettext_lazy as _


class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Group
        fields = ["name", "permissions"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        meus_apps = [
            "customers",
            "finances",
            "tasks",
            "users",
        ]
        content_types = ContentType.objects.filter(app_label__in=meus_apps)
        self.fields["permissions"].queryset = Permission.objects.filter(
            content_type__in=content_types
        )
        self.fields["permissions"].label_from_instance = self.permissions_label

    def permissions_label(self, obj) -> str:
        name_permission = obj.name
        name_permission = name_permission.replace("add", str(_("adicionar")))
        name_permission = name_permission.replace("change", str(_("alterar")))
        name_permission = name_permission.replace("delete", str(_("excluir")))
        name_permission = name_permission.replace("view", str(_("visualizar")))
        name_permission = name_permission.replace("Can", str(_("Pode")))
        return name_permission
