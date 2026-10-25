"""
Rotas da API (prefixo `/api/`).

Registre os ViewSets no router:

    router.register("produtos", ProdutoViewSet, basename="produto")
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

urlpatterns = [
    path("status/", views.status_api, name="status-api"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("", include(router.urls)),
]
