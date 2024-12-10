from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Login e Logout
    path(
        "",
        RedirectView.as_view(url="/login/", permanent=False),
        name="redirect_view",
    ),
    path("financeiro/", include("finances.urls")),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("admin/", admin.site.urls),
    path("usuarios/", include("users.urls")),
    path("clientes/", include("customers.urls")),
    path("tarefas/", include("tasks.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
