"""Models da API."""

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class UsuarioManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError("O e-mail é obrigatório.")
        usuario = self.model(email=email.strip().lower(), **extra)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault("is_staff", True)
        extra.setdefault("is_superuser", True)
        extra.setdefault("perfil", Usuario.Perfil.CEO)
        return self.create_user(email, password, **extra)


class Usuario(AbstractUser):
    """Usuário do Fast Horas: entra com e-mail e senha; `is_active` indica ativo/inativo."""

    class Perfil(models.TextChoices):
        CEO = "CEO", "CEO"
        GESTOR = "GESTOR", "Gestor"
        FUNCIONARIO = "FUNCIONARIO", "Funcionário"

    username = None
    email = models.EmailField("e-mail", unique=True)
    perfil = models.CharField("perfil", max_length=12, choices=Perfil.choices)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UsuarioManager()

    class Meta:
        verbose_name = "usuário"
        verbose_name_plural = "usuários"

    def __str__(self):
        return self.email
