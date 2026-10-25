"""
Models da API.

Crie aqui os models do domínio do projeto (nomes em português), por exemplo:

    class Produto(models.Model):
        nome = models.CharField("nome", max_length=100)
        preco = models.DecimalField("preço", max_digits=10, decimal_places=2)
        criado_em = models.DateTimeField("criado em", auto_now_add=True)

        class Meta:
            verbose_name = "produto"
            verbose_name_plural = "produtos"

        def __str__(self):
            return self.nome

Depois de criar ou alterar um model, rode `makemigrations` e `migrate`.
"""

from django.db import models  # noqa: F401
