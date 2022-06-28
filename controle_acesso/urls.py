from re import template
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from dashboard.views import index
from veiculos.views import (
    saida_veiculos, registrar_saida, informacoes_saida, veiculo_retorno
    )

from visitantes.views import (
    registrar_visitante, informacoes_visitantes, finalizar_visita
)
urlpatterns = [
    path("admin/", admin.site.urls),
    
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html"
        ),
        name="login"
    ),
    
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="logout.html"
        ),
        name="logout"
    ),
    
    path(
        "",
        index,
        name="index"
    ),
    path(
        "filtro/<int:f>/",
        index,
        name="filtro"
    ),
    path(
        "saida-veiculos",
        saida_veiculos,
        name="saida_veiculos"
    ),
    path(
        "registrar-visitante/", registrar_visitante,
        name="registrar_visitante"
    ),
    path(
        "registrar-saida/", registrar_saida,
        name="registrar_saida"
    ),
    path(
        "visitantes/<int:id>/",
        informacoes_visitantes,
        name= "informacoes_visitantes"
    ),
    path(
        "veiculo/<int:id>/",
        informacoes_saida,
        name="informacoes_saida"
    ),
    path(
        "visitantes/<int:id>/finalizar-visita",
        finalizar_visita,
        name="finalizar_visita"
    ),
    path(
        "veiculo/<int:id>/veiculo-retorno",
        veiculo_retorno,
        name="veiculo_retorno"
    ),
  
]
