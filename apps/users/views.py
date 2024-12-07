from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import Users
from .forms import UserCreateForm, UserEditForm
from django.urls import reverse_lazy


# Mixin para restringir ações apenas para superusuários
class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


# Listar usuários: Superusuários veem todos; usuários comuns veem apenas seus próprios registros
class UserListView(LoginRequiredMixin, ListView):
    model = Users
    template_name = "users/user_list.html"
    context_object_name = "users"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Users.objects.all()  # Superusuários veem todos os registros
        return Users.objects.filter(
            id=self.request.user.id
        )  # Usuários comuns veem apenas seus próprios registros


# Criar usuários: Apenas superusuários podem acessar
class UserCreateView(LoginRequiredMixin, SuperUserRequiredMixin, CreateView):
    model = Users
    form_class = UserCreateForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user-list")


# Editar usuários: Superusuários podem editar qualquer usuário; usuários comuns só editam seu próprio registro
class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Users
    form_class = UserEditForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user-list")

    def test_func(self):
        # Permitir apenas superusuários ou o próprio usuário
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user

    def form_valid(self, form):
        # Verifica se há uma nova senha no formulário
        password1 = form.cleaned_data.get("password1")
        if password1:
            self.object.set_password(password1)  # Atualiza a senha
        return super().form_valid(form)


# Excluir usuários: Apenas superusuários podem acessar
class UserDeleteView(LoginRequiredMixin, SuperUserRequiredMixin, DetailView):
    model = Users
    template_name = "users/user_confirm_delete.html"
    success_url = reverse_lazy("user-list")


# Detalhes do usuário: Superusuários podem acessar todos; usuários comuns podem acessar apenas seus próprios registros
class UserDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Users
    template_name = "users/user_detail.html"
    context_object_name = "user"

    def test_func(self):
        user = self.get_object()
        return self.request.user.is_superuser or self.request.user == user
