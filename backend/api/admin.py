"""Registro dos models no Django Admin."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from api.models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    ordering = ["email"]
    list_display = ["email", "perfil", "is_active"]
    search_fields = ["email"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Perfil", {"fields": ("perfil", "first_name", "last_name")}),
        ("Permissões", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "perfil", "password1", "password2")}),
    )
