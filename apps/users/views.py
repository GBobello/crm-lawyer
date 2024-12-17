from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView, View
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from .models import Users
from .forms import UserCreateForm, UserEditForm
from django.db.models import Q
import csv
import datetime

# Importações adicionais para gerar PDFs
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.utils import timezone
import textwrap


# Mixin para restringir ações apenas para superusuários
class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class UserExportCsvView(LoginRequiredMixin, View):
    model = Users
    context_object_name = "users"

    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = (
            "attachment; filename=Usuarios" + str(datetime.datetime.now()) + ".csv"
        )

        writer = csv.writer(response)
        writer.writerow(["Nome", "Email", "Telefone", "Nível", "Ativo"])
        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"
        if search:
            Users2 = Users.objects.filter(
                Q(username__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
            ).order_by(orderby)
        else:
            Users2 = Users.objects.all().order_by(orderby)

        for user in Users2:
            writer.writerow(
                [
                    user.username,
                    user.email,
                    user.telefone_formatado(),
                    "Admin" if user.is_superuser else "Escritorio",
                    "Sim" if user.is_active else "Não",
                ]
            )

        return response

class UserExportPDFView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=Usuarios_{timezone.now().strftime("%Y-%m-%d_%H-%M-%S")}.pdf'

        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter

        p.setFont("Helvetica-Bold", 16)
        p.drawString(30, height - 50, "Relatório de Usuários")

        headers = [
            "Nome",
            "Email",
            "Telefone",
            "Nível",
            "Ativo"
        ]

        p.setFont("Helvetica-Bold", 8)
        x_offsets = [30, 120, 200, 270, 340, 380, 440]
        y = height - 80
        for i, header in enumerate(headers):
            p.drawString(x_offsets[i], y, header)

        p.line(30, y - 5, width - 30, y - 5)

        search = self.request.GET.get("search")
        orderby = self.request.GET.get("orderby")
        if not orderby:
            orderby = "id"
        if search:
            Users2 = Users.objects.filter(
                Q(username__icontains=search)
                | Q(email__icontains=search)
                | Q(telefone__icontains=search)
            ).order_by(orderby)
        else:
            Users2 = Users.objects.all().order_by(orderby)

        p.setFont("Helvetica", 8)
        y = height - 100
        line_height = 14

        for user in Users2:
            texts = [
                    user.username,
                    user.email,
                    user.telefone_formatado(),
                    "Admin" if user.is_superuser else "Escritorio",
                    "Sim" if user.is_active else "Não",
            ]

            
            max_lines = 1
            for i, text in enumerate(texts):
                wrapped_text = p.beginText(x_offsets[i], y)
                lines = textwrap.wrap(text, width=15) 
                max_lines = max(max_lines, len(lines))
                for line in lines:
                    wrapped_text.textLine(line)
                p.drawText(wrapped_text)

            y -= max_lines * line_height

            if y < 50:
                p.showPage()
                y = height - 50

                p.setFont("Helvetica-Bold", 12)
                for i, header in enumerate(headers):
                    p.drawString(x_offsets[i], y, header)
                p.line(30, y - 5, width - 30, y - 5)
                p.setFont("Helvetica", 10)
                y = height - 100

        p.showPage()
        p.save()

        return response



class UserMessageView(LoginRequiredMixin, View):
    context_object_name = "message"

    def get(self, request, *args, **kwargs):
        # Aqui você pode definir a mensagem que deseja passar como resposta JSON
        response_data = {
            "message": "Operação concluída com sucesso!",
            "status": "success",
        }
        # Retorna a resposta JSON
        return JsonResponse(response_data)


# Listar usuários: Superusuários veem todos; usuários comuns veem apenas seus próprios registros
class UserListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Users
    template_name = "users/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        if self.request.user.is_superuser:
            search = self.request.GET.get("search")
            orderby = self.request.GET.get("orderby")
            if not orderby:
                orderby = "id"
            if search:
                return Users.objects.filter(
                    Q(username__icontains=search)
                    | Q(email__icontains=search)
                    | Q(telefone__icontains=search)
                ).order_by(orderby)

            return Users.objects.all().order_by(orderby)
            # Superusuários veem todos os registros
        return Users.objects.filter(id=self.request.user.id).order_by(
            orderby
        )  # Usuários comuns veem apenas seus próprios registros

    def get_template_names(self):
        content = self.request.META.get("CONTENT_TYPE")
        if content and "application/text" in content:
            return ["users/user_list_table.html"]
        else:
            return [self.template_name]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adiciona a lista de campos ao contexto
        context["fields"] = {
            "id": "Código",
            "username": "Nome",
            "email": "Email",
            "telefone": "Telefone",
            "is_superuser": "Nível",
            "is_active": "Ativo",
        }
        context["name_model"] = "Usuário"
        context["plural_name_model"] = "Usuários"
        return context


# Criar usuários: Apenas superusuários podem acessar
class UserCreateView(LoginRequiredMixin, SuperUserRequiredMixin, CreateView):
    model = Users
    form_class = UserCreateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user-message")

    def form_valid(self, form):
        # Chama o método da superclasse para salvar o objeto
        form.instance.is_active = True  # Mater assim até ajustar

        response = super().form_valid(form)
        # Adiciona uma mensagem de sucesso
        messages.success(self.request, "Usuário criado com sucesso!")
        # Retorna a resposta
        return response


# Editar usuários: Superusuários podem editar qualquer usuário; usuários comuns só editam seu próprio registro
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Users
    form_class = UserEditForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user-message")

    def test_func(self):
        # Permitir apenas superusuários ou o próprio usuário
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user

    def form_valid(self, form):
        # Verifica se há uma nova senha no formulário
        form.instance.is_active = True  # Mater assim até ajustar
        password1 = form.cleaned_data.get("password1")
        if password1:
            self.object.set_password(password1)  # Atualiza a senha

        response = super().form_valid(form)
        messages.success(self.request, "Usuário atualizado com sucesso!")
        return response


# Excluir usuários: Apenas superusuários podem acessar
class UserDeleteView(LoginRequiredMixin, SuperUserRequiredMixin, DetailView):
    model = Users
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user-message")


# Detalhes do usuário: Superusuários podem acessar todos; usuários comuns podem acessar apenas seus próprios registros
class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Users
    template_name = "users/user_detail.html"
    context_object_name = "user"

    def test_func(self):
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user
